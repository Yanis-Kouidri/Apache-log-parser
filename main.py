# !/usr/bin/python3

import argparse  # Module qui permet de passer des arguments, très pratique

import fonctions  # Toutes les fonctions que nous avons codées

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
print()
if args.stats:
    liste_de_dico = fonctions.json_vers_dico(args.output_file)  # Je crée une liste de dico avec tous les champs
    # à partir de mon json

    # Puis je fais des stats pour tous les champs intéressant
    stats_reponse = fonctions.compteur(liste_de_dico, 'response')
    fonctions.affichage_stat(stats_reponse)
    fonctions.def_code_retour()  # Explication textuelle des différents type de codes retour
    print()
    stats_log_code = fonctions.compteur(liste_de_dico, "log_code")
    fonctions.affichage_stat(stats_log_code)
    fonctions.def_log_code()
    print()
    stat_system_agent = fonctions.compteur(liste_de_dico, "system_agent")
    fonctions.affichage_stat(stat_system_agent)
