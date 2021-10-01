#!/usr/bin/python3

import re

def whatis (resultat):       #Affiche le résulatat d'un re.search, si c'est vide, retourne none.
    if resultat == None:
        print (resultat)
    else:
        print (resultat.group(0))


with open('./ten_logs', 'r') as ten:
    for ligne in ten:
        ip=re.search("([0-9]{1,3}\.){3}[0-9]{1,3}", ligne)
        whatis(ip)
        date = re.search("\[[1-3][0-9]/[A-Z][a-z]{2}/[0-9]{4}(:[0-9]{2}){3} [-\+][0-9]{4}\]", ligne)
        whatis(date)
        get = re.search('"GET /[^"]*"', ligne)
        whatis(get)


        print("\n")







