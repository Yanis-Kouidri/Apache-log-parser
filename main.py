# !/usr/bin/python3

import argparse  # Module qui permet de passer des arguments, très pratique

import fonctions

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Le chemin et le nom du fichier contenant les logs apaches brutes"
                                       " Ex : /var/log/apache/log", type=str)
parser.add_argument("output_file", help="Le chemin et le nom du fichier de sortie que le programme va créer,"
                                        " ce sera un fichier json Ex : /home/Documents/mon_json.json", type=str)
parser.add_argument("-s", "--stats", help="Permet d'afficher des statistiques à partir du json créé",
                    action="store_true")
args = parser.parse_args()

# print(args.input_file)

deconcat = fonctions.deconcatenation(args.input_file)
reparti = fonctions.repartition(deconcat)
fonctions.dico_vers_json(reparti, args.output_file)
if args.stats:
    liste_de_dico = fonctions.json_vers_dico(args.output_file)
    stats_reponse = fonctions.compteur(liste_de_dico,'response')
    print(f"Sur un total de {stats_reponse['total']} champs response")
    for code, nombre in stats_reponse.items():
        if code != 'total':
            print(f"Il y a {nombre} réponses {code}")

