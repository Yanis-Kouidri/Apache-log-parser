#!/usr/bin/python3

import json
import re
import deconcat


def prejson (tableaulog):          #permet de donner une clé aux valeur obtenues grâce à parsing()
    tableau_pre_json=[]
    for ligne in tableaulog:
        lignejson = {}
        if deconcat.whatis(re.search('([0-9]{1,3}\.){3}[0-9]{1,3}', ligne[0])) is not "-":          #Je regarde si le premier champ est une adresse IP ou autre chose
            lignejson['IP']=ligne[0]
        else:
            lignejson['host_name']=ligne[0]            #Si ce n'est pas une IP c'est le nom de l'hote (très rare)

        lignejson['client_id']=ligne[1]
        lignejson['user_id']=ligne[2]
        lignejson['date']=ligne[3]
        lignejson['query']=ligne[4]
        
        lignejson['query_type']=deconcat.whatis(re.search('(?<=")[^ ]*(?= )', ligne[4]))      #Je récupère l'action effectué (GET, HEAD, POST)
        lignejson['query_what']=deconcat.whatis(re.search('(?<= )[^ ]*(?= )', ligne[4]))      #Je récupère l'action effectué (GET, HEAD, POST)
        lignejson['query_how']=deconcat.whatis(re.search('((?<= )[^ ]*(?= ))/2', ligne[4]))      #Je récupère l'action effectué (GET, HEAD, POST)

        lignejson['status_code']=ligne[5]
        lignejson['object_size']=ligne[6]
        lignejson['referer']=ligne[7]
        lignejson['user_agent']=ligne[8]
        lignejson['log_code']=ligne[9]



        tableau_pre_json.append(lignejson)
    return tableau_pre_json

#print(prejson(deconcat.parsing1('logs_sabotes')))
deconcat.afficher3(prejson(deconcat.parsing1('ten_logs')))
#deconcat.afficher3(deconcat.parsing1('logs_sabotes'))
