# !/usr/bin/python3

# Définition de toutes les fonctions nécessaires au fonctionnement du programme
# Ces fonctions seront appelées dans la main

import re
import json
import statistics


def plein_ou_vide(search):  # Petite fonction qui nous dis si une regexp est un succès ou non
    if search:
        return search.group(0)
    else:
        return "-"


def deconcatenation(
        fichier):  # Dans un premier temps je découpe chaque log en fonction des champs
    # et je retourne une liste de liste ou chaque case est un champs du log
    with open(fichier, 'r') as les_logs:
        liste_de_logs = []
        for un_log in les_logs:
            liste_pour_un_log = []
            decoupage1 = re.search('(\S*) (\S*) (\S*) (\[[^]]*]) ("[^"]*") (\S*) (\S*) ("[^"]*") ("[^"]*")',
                                   un_log)  # Découpage un log complet (avec 9 champs)
            if decoupage1 is None:
                decoupage1 = re.search('(\S*) (\S*) (\S*) (\[[^]]*]) ("[^"]*") (\S*) (\S*)',
                                       un_log)  # découpage pour un log auquel il manque les deux derniers champs
                # (ils sont facultatifs) (donc 7 champs)
                if decoupage1 is None:  # Si vraiment la ligne n'arrive pas à être découpée,
                    # alors on rentre tous les champs avec -
                    for i in range(9):
                        liste_pour_un_log.insert(i, "-")
                    liste_pour_un_log.append("KO")  # Je précise dans la 10eme entrée du tableau que le log est KO
                else:
                    for i in range(7):
                        liste_pour_un_log.insert(i, decoupage1.group(
                            i + 1))  # i+1 car le 0 correspond à la regexp en entier
                    liste_pour_un_log.append("-")  # Pour faire le tare jusqu'à 9
                    liste_pour_un_log.append("-")  # Pour faire le tare jusqu'à 9
                    liste_pour_un_log.append("OK")  # Je précise dans la 10eme entrée du tableau que le log est OK
            else:
                for i in range(9):
                    liste_pour_un_log.insert(i,
                                             decoupage1.group(i + 1))  # i+1 car le 0 correspond à la regexp en entier
                liste_pour_un_log.append("OK")  # Je précise dans la 10eme entrée du tableau que le log est OK

            liste_de_logs.append(liste_pour_un_log)
        return liste_de_logs


# liste_de_liste10 = deconcatenation('ten_logs') # lignes de test
# liste_de_liste_tout = deconcatenation('apache_logs')


def repartition(liste_de_liste):  # Fonction qui va attribuer chaque case de la liste dans un dictionnaire
    liste_de_dico = []
    for tableau_dun_log in liste_de_liste:
        dico_dun_log = {}
        dico_dun_log['remote_ip'] = tableau_dun_log[0]
        dico_dun_log['client_id'] = tableau_dun_log[1]
        dico_dun_log['user_id'] = tableau_dun_log[2]
        dico_dun_log['time'] = tableau_dun_log[3]
        dico_dun_log['request'] = tableau_dun_log[4]

        request_champs = re.search('"(\S*) (\S*) ([^"]*)"', tableau_dun_log[
            4])  # je découpe le champ request en sous champs,
        # l'un étant le type de requête, le suivant le fichier demandé et le dernier le protocole HTTP utilisé
        if request_champs:
            dico_dun_log['request_type'] = request_champs.group(1)  # Je rentre l'action effectué (GET, HEAD, POST)
            dico_dun_log['request_what'] = request_champs.group(
                2)  # Je rentre le fichier demandé (dans le cas d'un GET)
            dico_dun_log['request_how'] = request_champs.group(3)  # Je rentre la version du protocole HTTP utilisé
        dico_dun_log['response'] = tableau_dun_log[5]  # Code de réponse
        dico_dun_log['bytes'] = tableau_dun_log[6]  # taille de l'objet demandé (vide si ce n'est pas un GET)
        dico_dun_log['referer'] = tableau_dun_log[7]
        dico_dun_log['user_agent'] = tableau_dun_log[8]
        dico_dun_log['system_agent'] = plein_ou_vide(
            re.search('Linux|Macintosh|Windows|iPhone|SAMSUNG|[Bb]ot', tableau_dun_log[
                8]))  # le système du client (il n'y a pas que ces 5 systèmes mais c'est déjà bien)
        dico_dun_log['log_code'] = tableau_dun_log[9]

        liste_de_dico.append(dico_dun_log)

    return liste_de_dico  # le return est une liste de dictionnaire,
    # dans un dictionnaire on trouve pour tous les champs d'un log : clé = nom du champ et valeur = valeur du champ
    # Exemple : ip = 88.54.17.154


# liste_de_dico10 = repartition(liste_de_liste10) # lignes de test
# liste_de_dico_tout = repartition(liste_de_liste_tout)


# for line in (repartition(deconcatenation('logs_sabotes'))):
#    print(line)


# for line in (repartition(liste_de_liste10)):
#    print(line)

def dico_vers_json(liste_de_dico, nom_du_fichier):  # Fonction qui à partir d'une liste de dictionnaires
    # fourni un fichier json où chaque objet est un dico d'un log
    with open(nom_du_fichier,
              'w') as fichier_json:  # On ouvre le fichier dans lequel on va inscrire les lignes au format json
        json.dump(liste_de_dico, fichier_json,
                  indent=4)  # l'indentation permet d'avoir un fichier plus lisible si jamais on doit l'ouvrir à la main
        print(f"{len(liste_de_dico)} lignes ont été écrites dans {nom_du_fichier}")


# dico_vers_json(liste_de_dico_tout, 'mon_json.json') # ligne de test


def json_vers_dico(nom_du_json):  # Fonction qui fait l'inverse de dico_vers_json
    # à partir d'un json elle fait une liste de dico
    with open(nom_du_json, 'r') as le_json:
        dic_log = json.load(le_json)
    return dic_log


# liste_de_dico_nouv = json_vers_dico('mon_json.json') # ligne de test


# print(liste_de_dico_nouv)
# for dico in liste_de_dico_nouv:
#    print(dico)


def compteur(tab_log,
             elem_log):  # fonction qui compte le nombre d'un élément du log
    # (ex : l'element response, on aura donc en sortie un dico avec comme clé 404 et comme valeur le nom
    stats = {'total': 0, 'type': elem_log}  # la clé
    for un_log in tab_log:  # Je rentre comme clé dans le dico stats chaque type d'erreur possible
        stats[un_log[elem_log]] = 0
    cles = stats.keys()
    for un_log in tab_log:  # Pour chaque log parsé, pour chaque clé, je regarde si c'est égal
        # (ce n'est pas hyper opti mais c'est pas trop mal)
        for cle in cles:
            if un_log[elem_log] == cle:
                stats[cle] = stats[cle] + 1
                stats['total'] = stats['total'] + 1  # Je compte le nombre total de log ayant un code de retour
    return stats


# code_retour = compteur(liste_de_dico_nouv, 'response')
# print(code_retour)


def pourcentage(
        stats):  # Fonction qui a partir d'un dico ayant pour cle un type et pour valeur un nombre
    # retourne le pourcentage par rapport au total
    # exemple : cle = '404' valeur = 35 (il y a donc 35 erreurs 404)
    # La fonction calcule donc le pourcentage d'erreurs 404 par rapport au total des requêtes
    # Elle fonctionne de pair avec compteur
    pourcent = {"type": stats["type"]}
    total = stats['total']

    for code, nombre in stats.items():
        if code != "type":
            pourcent[code] = round((nombre / total) * 100,
                                   2)  # round permet d'arondir le pourcentage 2 chiffres après la virgule
    return pourcent


def affichage_stat(stats):  # fonction qui affiche les stats après un compteur
    print(f"Sur un total de {stats['total']} champs {stats['type']}")
    for code, nombre in stats.items():
        if code != 'total' and code != 'type':
            print(f"Il y a {nombre} {stats['type']} {code}")


def affichage_stat_pourcent(stats):  # fonction qui affiche les stats après un compteur
    print(f"Sur un total de {stats['total']} % de champs {stats['type']}")
    for code, nombre in stats.items():
        if code != 'total' and code != 'type':
            print(f"Il y a {nombre} % de {stats['type']} {code}")


def calcul_poids(liste_dico):  # fonction qui fournit des stats à partir de l\'élément bytes
    liste_byte = []
    for dico in liste_dico:
        if dico['bytes'] != '-':
            liste_byte.append(int(dico['bytes']))
    mediane = statistics.median(liste_byte)
    moyenne = round(statistics.fmean(liste_byte))
    nb_objet = len(liste_byte)
    total = sum(liste_byte)
    variance = round(statistics.variance(liste_byte, moyenne))
    ecart_type = round(statistics.stdev(liste_byte, moyenne))
    minimum = min(liste_byte)
    maximum = max(liste_byte)
    stats_poids = {"Somme de tous les objets": total, "Nombre d'objets": nb_objet, "Moyenne": moyenne,
                   "Médiane": mediane, "Variance": variance,
                   "Écart-type": ecart_type, "Plus petit objet": minimum, "Plus grand objet": maximum}
    return stats_poids


def affichage_stat_poids(stats_poids):
    for nom, valeur in stats_poids.items():
        if nom == "Variance" or nom == "Écart-type":
            print(f"{nom} = {valeur}")
        else:
            print(f"{nom} = {valeur} octets")


def def_code_retour():
    print()
    print("Définition des codes de réponse les plus importants :")
    print("Les réponses ayant un code 200 sont les réponses OK, elles doivent être très majoritaires")
    print("Les réponses ayant un code 404 indiquent que l\'utilisateur tente d\'accéder à un fichier qui n\'existe pas"
          "Si la plupart de ces codes 404 se concentrent sur un même objet, cela veut probablement dire qu\'il existait"
          "auparavant et qu\'il a été déplacé,"
          " dans ce cas il faudrait mettre une redirection vers le nouvel objet là où"
          " les codes 404 tentent d\'accéder")
    print("Les réponses ayant un code 403 indiquent que l\'utilisateur tente d\'acceder à un objet auquel il ne devrait"
          " pas (forbidden). S\'il y en a beaucoup de la même adresse IP cela est très suspect.")
    print("Les réponses ayant un code 500 indiquent une erreur de la part du serveur. Il ne doit pas y en avoir, toutes"
          " erreur 500 est un client de moins sur notre site. Elles sont donc très critiques.")


# pourcent_response = pourcentage(code_retour)
# print(pourcent_response)

def def_log_code():
    print()
    print("Les log_code OK correspondent aux logs qui ont pu être correctement déconcaténé donc des logs valides")
    print("Les log_code KO correspondent aux logs qui n\'ont pas pu être déconcaténé donc qui ont mal été générés par "
          "le serveur. Cela peut arriver, mais s\'il y en a trop cela est inquiétant quant au serveur")


def def_system_agent():
    print()
    print("Ces statistiques peuvent être intéressantes notamment pour savoir s\'il y a beaucoup de mobiles qui"
          " consultent le site web")
