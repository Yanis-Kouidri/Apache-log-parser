#!/usr/bin/python3

#Ce fichier python a pour but, à partir d'un fichier .json généré par json_maker.py de généré des statistiques
#Dans un premier temps j'ouvre mon fichier json et j'en extrais les informations

import json
#import re
#import deconcat

def json_opener (le_json):      #Cette fonction permet d'ouvrir un json et de le transformer en tableau de dictionnaire avec dans chaque dico les éléments
    with open(le_json, 'r') as data_json:
        tableau_de_log = []
        dic_log = json.load(data_json)
        tableau_de_log.append(dic_log)
    return tableau_de_log
print(json_opener('log.json')[1])      #pour le déboggage
tab_log = json_opener('log.json')



def pourcentage (stats):        #Fonction qui a partir d'un dico ayant pour cle un type et pour valeur un nombre retourne le pourcentage par rapport au total
    pourcent = {}
    total = stats['total']
    for code, nombre in stats.items():
        pourcent[code] = (nombre/total)*100
    return pourcent

def compteur (tab_log, elem_log):         #fonction qui compte le nombre d'un élément du log (ex : l'element response, on aura donc en sortie un dico avec comme clé 404 et comme valeur le nom
    stats = {}      #la clé
    stats['total'] = 0
    for un_log in tab_log:          #Je rentre comme clé dans le dico stats chaque type d'erreur possible
        stats[un_log[elem_log]] = 0
    cles = stats.keys()
    for un_log in tab_log:          #Pour chaque log parsé, pour chaque clé, je regarde si c'est égal (c'est pas hyper opti mais c'est pas trop mal)
        for cle in cles:
            if un_log[elem_log] == cle:
                stats[cle] = stats[cle] + 1
                stats['total'] = stats['total'] + 1     #Je compte le nombre total de log ayant un code de retour
    return stats

nb_code_reponse = compteur(tab_log, 'response')
print(compteur(tab_log, 'response'))
print(pourcentage(nb_code_reponse))
print(compteur(tab_log, 'system_agent'))
print('ok')