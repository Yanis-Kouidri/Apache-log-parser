#!/usr/bin/python3

import re

def whatis (resultat):       #Retroune le résulatat d'un re.search, si c'est vide, retourne none.
    if resultat is None:
        return resultat
    else:
        return resultat.group(0)

def parsing1 (log):                     #Le but de cette fonction est de prendre les 9 éléments qui constituent un log apache de la manière la plus brute possible. A chaque fois qu'on récupère un élément, on croque la ligne (on lui enlève cet élément)
    with open(log, 'r') as ten:        #On ouvre le fichier ten_logs qui contient les 10 premières lignes de log apache (pour éviter d'en parcourir 50000)
        elements=[]
        for ligne in ten:
            item1 = whatis(re.search('[^ ]* ', ligne))
            elements.append(item1)
            ligne = ligne[len(item1):]
            item2 = whatis(re.search('[^ ]* ', ligne))
            elements.append(item2)
            ligne = ligne[len(item2):]
            item3 = whatis(re.search('[^ ]* ', ligne))
            elements.append(item3)
            ligne = ligne[len(item3):]
            item4 = whatis(re.search("\[[^\]]*\] ", ligne))     #Je suis volontèrement peu séléctif car le format de la date et de l'heure peuvent être modifié
            elements.append(item4)
            ligne = ligne[len(item4):]
            item5 = whatis(re.search('"[^"]*" ', ligne))
            elements.append(item5)
            ligne = ligne[len(item5):]
            item6 = whatis(re.search('[^ ]* ', ligne))
            elements.append(item6)
            ligne = ligne[len(item6):]
            item7 = whatis(re.search('[^ ]* ', ligne))
            elements.append(item7)
            ligne = ligne[len(item7):]
            item8 = whatis(re.search('"[^"]*" ', ligne))
            elements.append(item8)
            ligne = ligne[len(item8):]
            item9 = whatis(re.search('"[^"]*"', ligne))
            elements.append(item9)
            ligne = ligne[len(item9):]
    return elements

print(parsing1("ten_logs"))


def parsing (log):
    with open(log, 'r') as ten:        #On ouvre le fichier ten_logs qui contient les 10 premières ligne de log apache (pour éviter d'en parcourir 50000) 
        resultats=[]
        for ligne in ten:                       #pour chaque ligne dans ce fichier on va essayer à l'aide d'expressions régulières de récupérer tous les champs.
            ip=re.search("([0-9]{1,3}\.){3}[0-9]{1,3}", ligne)          #recherche la première adresse IP de la ligne donc a priori celle du client
            #whatis(ip)
            date = re.search("\[[1-3][0-9]/[A-Z][a-z]{2}/[0-9]{4}(:[0-9]{2}){3} [\-\+][0-9]{4}\]", ligne)        # recherche la date selon le format des logs apache
            #whatis(date)
            get = re.search('"GET /[^"]*"', ligne)          #Si l'utilisateur a fait un GET, recherche le get fait par l'utilisateur
            #whatis(get)
            get_and_codes = re.search('"GET /[^"]*" [1-5][0-9]{2} [0-9]*', ligne)         #Prends le Get plus le code de retour (RFC2616) plus la taille de l'objet demandé par le client (sans les en-têtes)
            #whatis(get_and_codes)
            get_to_end = re.search('"GET /[^"]*" [1-5][0-9]{2} [0-9]* "[^"]*" "[^"]*"', ligne)         #Le get, les codes plus les deux champs correspondant à l'en-tête referer (le lien sur lequel le client est) et l'en-tête user-agent de la requête HTTP
            #whatis(get_to_end)
            champs= {'ip': whatis(ip), 'date': whatis(date), 'get': whatis(get), 'get_and_codes': whatis(get_and_codes),
                     'get_to_end': whatis(get_to_end)}

            codes = champs['get_and_codes'][len(champs['get']):]         #à partir de get et get_and_codes, je prends juste la différence des deux à l'aide de la taille de get comme ça j'ai les deux code (code retour et taille)
            codes = codes.split(' ')                              #Je split les deux codes en utilisant l'espace et je les rentres dans le dico
            champs['coderetour']=codes[1]
            champs['tailleobj']=codes[2]
            if get_to_end is not None:      #Si get_to_end est défini cela veut dire qu'il y a les champs referer et user-agent donc on les capture sinon on les remplit avec du vide
                dernier_champs = champs['get_to_end'][len(champs['get_and_codes']):]  # Je fais la même chose que précédemmment mais avec les deux derniers champs du log
                dernier_champs = re.findall('"[^"]*"', dernier_champs)

                #print("\n")
                champs['referer'] = dernier_champs[0]
                champs['user_agent'] = dernier_champs[1]
            else:
                champs['referer'] = "-"
                champs['user_agent'] = "-"

            resultats.append(champs)
    return resultats 
            
#parsing('ten_logs2')


def afficher (tableaulog):          #permet d'afficher le contenu du tableau de dictionnaire retourné par la fonction parsing
    for ligne in tableaulog:
        for cle,valeur in ligne.items():
            if valeur is not None:
                print(cle+'='+valeur)
            else:
                print(cle+"= ")
        print()

#afficher(parsing('ten_logs2'))
#afficher(parsing('ten_logs2'))


