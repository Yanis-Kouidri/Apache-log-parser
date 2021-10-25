# !/usr/bin/python3

import re
import json


def plein_ou_vide(search):  # Petite fonction qui nous dis si une regexp est un succès ou non
    if search:
        return search.group(0)
    else:
        return "-"


def deconcatenation(
        fichier):  # Dans un premier temps je découpe chaque log en fonction des champs et je retourne une liste de liste ou chaque case est un champs du log
    with open(fichier, 'r') as les_logs:
        liste_de_logs = []
        for un_log in les_logs:
            liste_pour_un_log = []
            decoupage1 = re.search('(\S*) (\S*) (\S*) (\[[^]]*]) ("[^"]*") (\S*) (\S*) ("[^"]*") ("[^"]*")',
                                   un_log)  # Découpage un log complet (avec 9 champs)
            if decoupage1 is None:
                decoupage1 = re.search('(\S*) (\S*) (\S*) (\[[^]]*]) ("[^"]*") (\S*) (\S*)',
                                       un_log)  # découpage pour un log auquel il manque les deux derniers champs (ils sont facultatifs) (donc 7 champs)
                if decoupage1 is None:  # Si vraiment la ligne n'arrive pas à être découpée, alors on rentre tous les champs avec -
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


liste_de_liste10 = deconcatenation('ten_logs')


def repartition(liste_de_liste):  # Fonction qui va attribuer chaque case de la liste dans un dictionnaire
    liste_de_dico = []
    for tableau_dun_log in liste_de_liste:
        dico_dun_log = {}
        dico_dun_log['remote_ip'] = tableau_dun_log[0]
        dico_dun_log['client_id'] = tableau_dun_log[1]
        dico_dun_log['user_id'] = tableau_dun_log[2]
        dico_dun_log['date'] = tableau_dun_log[3]
        dico_dun_log['request'] = tableau_dun_log[4]

        request_champs = re.search('"(\S*) (\S*) ([^"]*)"', tableau_dun_log[
            4])  # je découpe le champ request en sous champs, l'un étant le type de requête, le suivant le fichier demandé et le dernier le protocole HTTP utilisé
        if request_champs:
            dico_dun_log['request_type'] = request_champs.group(1)  # Je rentre l'action effectué (GET, HEAD, POST)
            dico_dun_log['request_what'] = request_champs.group(
                2)  # Je rentre le fichier demandé (dans le cas d'un GET)
            dico_dun_log['request_how'] = request_champs.group(3)  # Je rentre la version du protocole HTTP utilisé
        dico_dun_log['response'] = tableau_dun_log[5]  # Code de réponse
        dico_dun_log['object_size'] = tableau_dun_log[6]  # taille de l'objet demandé (vide si ce n'est pas un GET)
        dico_dun_log['referer'] = tableau_dun_log[7]
        dico_dun_log['user_agent'] = tableau_dun_log[8]
        dico_dun_log['system_agent'] = plein_ou_vide(
            re.search('Linux|Macintosh|Windows|iPhone|SAMSUNG', tableau_dun_log[
                8]))  # le système du client (il n'y a pas que ces 4 systèmes mais c'est déjà bien)
        dico_dun_log['log_code'] = tableau_dun_log[9]

        liste_de_dico.append(dico_dun_log)

    return liste_de_dico  # le return est une liste de dictionnaire, dans un dictionnaire on trouve pour tous les champs d'un log : clé = nom du champ et valeur = valeur du champ Exemple : ip = 88.54.17.154


liste_de_dico10 = repartition(liste_de_liste10)

for line in (repartition(deconcatenation('logs_sabotes'))):
    print(line)


# for line in (repartition(liste_de_liste10)):
#    print(line)

def vers_un_json(liste_de_dico, nom_du_fichier):
    with open(nom_du_fichier,
              'w') as fichier_json:  # On ouvre le fichier dans lequel on va inscrire les lignes au format json
        print(f"J'ai écrit {len(liste_de_dico)} ligne(s) dans {nom_du_fichier}")
        json.dump(liste_de_dico, fichier_json,
                  indent=4)  # l'indentation permet d'avoir un fichier plus lisible si jamais on doit l'ouvrir à la main


vers_un_json(liste_de_dico10, 'mon_json.json')

