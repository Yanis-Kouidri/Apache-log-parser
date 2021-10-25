# !/usr/bin/python3

import re

def deconcatenation (fichier):  # Dans un premier temps je découpe chaque log en fonction des champs et je retourne une liste de liste ou chaque case est un champs du log
    with open(fichier, 'r') as les_logs:

        for un_log in les_logs:
            decoupage1 = re.search('(\S*) (\S*) (\S*) (\[[^]]*]) ("[^"]*") (\S*) (\S*) ("[^"]*") ("[^"]*")', un_log)   # Découpage un log complet (avec 9 champs)
            if decoupage1 is None:
                decoupage1 = re.search('(\S*) (\S*) (\S*) (\[[^]]*]) ("[^"]*") (\S*) (\S*)', un_log)   # découpage pour un log auquel il manque les deux derniers champs (ils sont facultatifs) (donc 7 champs)
            if decoupage1 is None:

            print(decoupage1.group(0))


deconcatenation('logs_sabotes')