#!/usr/bin/python3

import json
import re
import deconcat


def prejson (tableaulog):          #permet de donner une clé aux valeur obtenues grâce à parsing()
    tableauprejson=[]
    for ligne in tableaulog:
        lignejson = {}
        if deconcat.whatis(re.search('([0-9]{1,3}\.){3}[0-9]{1,3}', ligne[0])) is not "-":          #Je regarde si le premier champ est une adresse IP ou autre chose
            lignejson['IP']=ligne[0]
        else:
            lignejson['host_name']=ligne[0]            #Si ce n'est pas une IP c'est le nom de l'hote (très rare)



        tableauprejson.append(lignejson)
    return tableauprejson

#prejson(deconcat.parsing1('ten_logs'))
print(prejson(deconcat.parsing1('logs_sabotes')))