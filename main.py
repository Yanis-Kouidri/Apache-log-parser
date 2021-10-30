# !/usr/bin/python3

import argparse  # Module qui permet de passer des arguments, très pratique
import os   # Je l'utilise pour voir si un fichier existe
import fonctions  # Toutes les fonctions que nous avons codées

parser = argparse.ArgumentParser()

parser.add_argument("json_file",
                    help="Le chemin et le nom du fichier que le programme va créer"
                         " si l'argument -l est utilisé, "
                         "sinon le json que le programme va lire pour afficher des statistiques,"
                         " ce sera un fichier json. Ex : /home/Documents/mon_json.json", type=str)
# L\'argument obligatoire, sans autre argument le programme va afficher les stats classique de ce json

parser.add_argument("-l", "--log_file", help="Le chemin et le nom du fichier contenant les logs apaches brutes."
                                             " Ex : /var/log/apache/log", type=str)

parser.add_argument("-s", "--stats", help="Permet d'afficher des statistiques à partir du json créé ou déjà existant."
                    , action="store_true")
parser.add_argument("-p", "--pourcent", help="Permet d'afficher des statistiques sous forme de pourcentages."
                    , action="store_true")
args = parser.parse_args()

# print(args.input_file)

if args.log_file:  # Si l'option -l est utilisée, on en fait un .json
    if os.path.isfile(args.log_file) is False:  # on vérifie que le fichier existe
        print(f"Le fichier de log {args.log_file} n'a pas pu être trouvé")
        exit(5)
    deconcat = fonctions.deconcatenation(args.log_file)
    reparti = fonctions.repartition(deconcat)
    fonctions.dico_vers_json(reparti, args.json_file)
    print()

if os.path.isfile(args.json_file) is False:  # on vérifie que le fichier existe
    print(f"Le fichier json {args.json_file} n'a pas pu être trouvé")
    exit(6)

if args.stats or (args.log_file is None and args.pourcent is False):  # Affichage des statistiques classiques

    liste_de_dico = fonctions.json_vers_dico(args.json_file)  # Je crée une liste de dico avec tous les champs
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
    fonctions.def_system_agent()
    print()
    stat_request_type = fonctions.compteur(liste_de_dico, "request_type")
    fonctions.affichage_stat(stat_request_type)
    print()
    stat_request_how = fonctions.compteur(liste_de_dico, "request_how")
    fonctions.affichage_stat(stat_request_how)
    print()
    stat_bytes = fonctions.calcul_poids(liste_de_dico)
    fonctions.affichage_stat_poids(stat_bytes)

if args.pourcent is True:  # Affichage des statistiques sous forme de pourcentage
    liste_de_dico = fonctions.json_vers_dico(args.json_file)  # Je crée une liste de dico avec tous les champs
    # à partir de mon json

    # Puis je fais des stats pour tous les champs intéressant
    stats_reponse = fonctions.compteur(liste_de_dico, 'response')
    stats_reponse = fonctions.pourcentage(stats_reponse)
    fonctions.affichage_stat_pourcent(stats_reponse)
    fonctions.def_code_retour()  # Explication textuelle des différents type de codes retour
    print()
    stats_log_code = fonctions.compteur(liste_de_dico, "log_code")
    stats_log_code = fonctions.pourcentage(stats_log_code)
    fonctions.affichage_stat_pourcent(stats_log_code)
    fonctions.def_log_code()
    print()
    stat_system_agent = fonctions.compteur(liste_de_dico, "system_agent")
    stat_system_agent = fonctions.pourcentage(stat_system_agent)
    fonctions.affichage_stat_pourcent(stat_system_agent)
    fonctions.def_system_agent()
    print()
    stat_request_type = fonctions.compteur(liste_de_dico, "request_type")
    stat_request_type = fonctions.pourcentage(stat_request_type)
    fonctions.affichage_stat_pourcent(stat_request_type)
    print()
    stat_request_how = fonctions.compteur(liste_de_dico, "request_how")
    stat_request_how = fonctions.pourcentage(stat_request_how)
    fonctions.affichage_stat_pourcent(stat_request_how)
