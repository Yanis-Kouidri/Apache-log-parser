#!/usr/bin/python3

import re

def whatis (resultat):       #Retroune le résulatat d'un re.search, si c'est vide, retourne "-".
    if resultat is None:
        return "-"
    else:
        return resultat.group(0)

def parsing1 (log):                     #Le but de cette fonction est de prendre les 9 éléments qui constituent un log apache de la manière la général possible. A chaque fois qu'on récupère un élément, on croque la ligne (on lui enlève cet élément)
    with open(log, 'r') as ten:        #On ouvre le fichier qui contient les logs apache
        entree=[]       #tableau dans lequel je mets des tableaux de champs

        for ligne in ten:
            elements = []       #tableau dans lequel je mets les champs d'une ligne
            item1 = whatis(re.search('[^ ]* ', ligne))          #adresse IP ou nom de l'hôte
            elements.append(item1[:-1])
            ligne = ligne[len(item1):]
            item2 = whatis(re.search('[^ ]* ', ligne))          #identité du client (très souvent vide)
            elements.append(item2[:-1])
            ligne = ligne[len(item2):]
            item3 = whatis(re.search('[^ ]* ', ligne))              #identifiant utilisateur, très souvent vide
            elements.append(item3[:-1])
            ligne = ligne[len(item3):]
            item4 = whatis(re.search("\[[^\]]*\] ", ligne))     #Date et heure de la requête, Je suis volontèrement peu séléctif car le format de la date et de l'heure peuvent être modifié
            elements.append(item4[:-1])
            ligne = ligne[len(item4):]
            item5 = whatis(re.search('"[^"]*" ', ligne))        #requête client, entre ""
            elements.append(item5[:-1])
            ligne = ligne[len(item5):]
            item6 = whatis(re.search('[0-9]* ', ligne))          #Code de statut, selon la RFC2616 ex 404
            elements.append(item6[:-1])
            ligne = ligne[len(item6):]
            item7 = whatis(re.search('[0123456789\-"]*', ligne))          #Taille de l'objet retourné au client sans les en-têtes, si pas d'objet alors "-"
            elements.append(item7)
            ligne = ligne[len(item7)+1:]
            item8 = whatis(re.search('"[^"]*" ', ligne))            #L'en-tête "Referer" de la requête HTTP. Il indique le site depuis lequel le client prétend avoir lancé sa requête.
            if item8 is "-":                                        #Si la regexp n'a rien trouvé, on met un tiret
                elements.append(item8)
            else:                                                   #Si la regexp a trouvé quelquechose (même un tiret, on enlève l'espace à la fin)
                elements.append(item8[:-1])
            ligne = ligne[len(item8):]
            item9 = whatis(re.search('"[^"]*"', ligne))                #L'en-tête User-Agent de la requête HTTP.
            elements.append(item9)
            ligne = ligne[len(item9):]
            if ligne is not "\n" or "":
                elements.append("error")
            #elements.append(ligne)     #la taille de la ligne doit être ici à zéro
            entree.append(elements)
    return entree           #retourne un tableau de tableau composé des neuf champs d'un log apache et eventuellement d'un champ avec error si la ligne n'a pas été totalement parsé

def afficher2 (tableaulog):          #permet d'afficher le contenu du tableau de dictionnaire retourné par la fonction parsing
    for ligne in tableaulog:
        for indice in ligne:
            print(indice)

        print()

def afficher3 (tableaulog):          #permet d'afficher le contenu du tableau de dictionnaire retourné par la fonction parsing
    for ligne in tableaulog:
        print(ligne)

#afficher3(parsing1("hundred_logs"))
afficher3(parsing1("apache_logs"))
#afficher3(parsing1("logs_sabotes"))
#afficher(parsing('ten_logs2'))
#afficher(parsing('ten_logs2'))


