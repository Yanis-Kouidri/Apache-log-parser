# !/usr/bin/python3

import argparse  # Module qui permet de passer des arguments, très pratique

import fonctions

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Le chemin et le nom du fichier contenant les logs apaches brutes"
                                       " Ex : /var/log/apache/log")
parser.add_argument("output_file", help="Le chemin et le nom du fichier de sortie que le programme va créer,"
                                        " ce sera un fichier json Ex : /home/Documents/mon_json.json")
args = parser.parse_args()

# print(args.input_file)

deconcat = fonctions.deconcatenation(args.input_file)
reparti = fonctions.repartition(deconcat)
fonctions.dico_vers_json(reparti, args.output_file)
