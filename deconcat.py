#!/usr/bin/python3

import re

def whatis (resultat):       #Affiche le résulatat d'un re.search, si c'est vide, retourne none.
    if resultat == None:
        print (resultat)
    else:
        print (resultat.group(0))


with open('./ten_logs', 'r') as ten:        #On ouvre le fichier ten_logs qui contient les 10 premières ligne de log apache (pour éviter d'en parcourir 50000) 
    for ligne in ten:                       #pour chaque ligne dans ce fichier on va essayer à l'aide d'expressions régulières de récupérer tous les champs.
        ip=re.search("([0-9]{1,3}\.){3}[0-9]{1,3}", ligne)          #recherche la première adresse IP de la ligne donc a priori celle du client
        whatis(ip)
        date = re.search("\[[1-3][0-9]/[A-Z][a-z]{2}/[0-9]{4}(:[0-9]{2}){3} [-\+][0-9]{4}\]", ligne)        # recherche la date selon le format des logs apache
        whatis(date)
        get = re.search('"GET /[^"]*"', ligne)          #Si l'utilisateur a fait un GET, recherche le get fait par l'utilisateur
        whatis(get)
        getAndCodes = re.search('"GET /[^"]*" [1-5][0-9]{2} [0-9]*', ligne)         #Prends le Get plus le code de retour (RFC2616) plus la taille de l'objet demandé par le client (sans les en-têtes) 
        whatis(getAndCodes)
        finligne = re.search('"GET /[^"]*" [1-5][0-9]{2} [0-9]* "[^"]*" "[^"]*"', ligne)         #Le get, les codes plus les deux champs correspondant à l'en-tête refer (le lien sur lequel le clien est) et l'en-tête user-agent de la requête HTTP
        whatis(finligne)


        print("\n")







