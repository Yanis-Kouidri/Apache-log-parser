#!/usr/bin/python3

import json
import re
import deconcat


def prejson (tableaulog):          #permet de donner une clé aux valeur obtenues grâce à parsing()
    tableau_pre_json=[]
    for ligne in tableaulog:
        lignejson = {}
        if deconcat.whatis(re.search('([0-9]{1,3}\.){3}[0-9]{1,3}', ligne[0])) is not "-":          #Je regarde si le premier champ est une adresse IP ou autre chose
            lignejson['remote_ip']=ligne[0]
        else:
            lignejson['host_name']=ligne[0]            #Si ce n'est pas une IP c'est le nom de l'hote (très rare)

        lignejson['client_id']=ligne[1]
        lignejson['user_id']=ligne[2]
        lignejson['date']=ligne[3]
        lignejson['request']=ligne[4]
        
        lignejson['request_type']=deconcat.whatis(re.search('(?<=")[^ ]*(?= )', ligne[4]))      #Je récupère l'action effectué (GET, HEAD, POST)
        lignejson['request_what']=deconcat.whatis(re.search('(?<= )[^ ]*(?= )', ligne[4]))      #Je récupère l'action effectué (GET, HEAD, POST)
        lignejson['request_how']=deconcat.whatis(re.search('((?<= )[^ ]*(?= ))/2', ligne[4]))      #Je récupère l'action effectué (GET, HEAD, POST)

        lignejson['response']=ligne[5]          #Code de réponse
        lignejson['object_size']=ligne[6]       #taille de l'objet demandé (vide si ce n'est pas un GET)
        lignejson['referer']=ligne[7]
        lignejson['user_agent']=ligne[8]
        lignejson['log_code']=ligne[9]



        tableau_pre_json.append(lignejson)
    return tableau_pre_json                 #le return est un tableau de dictionnaire, dans un dictionnaire on trouve pour tous les champs d'un log : clé = nom du champ et valeur = valeur du champ Exemple : ip = 88.54.17.154

tableau_pre_json = prejson(deconcat.parsing1('ten_logs'))

#print(prejson(deconcat.parsing1('logs_sabotes')))
#deconcat.afficher3(prejson(deconcat.parsing1('ten_logs')))
#deconcat.afficher3(deconcat.parsing1('logs_sabotes'))


def json_maker (pre_json):
    with open('log.json', 'w+') as fichier_json:        #On ouvre le fichier dans lequel on va inscrire les lignes au format json
        for dic in pre_json:
            fichier_json.write(json.dumps(dic)+"\n")
        
json_maker(tableau_pre_json)
#print(json.dumps(tableau_pre_json[0], indent=4))
#print(tableau_pre_json[0])
