# Projet-Python
Projet scolaire de python à l'IUT Réseaux et Télécommunications de l'université Nice Côte d'Azur dans le cadre du module M3206 "Automatisation des tâches d'administration.
Réalisé par JUST Maxime et KOUIDRI Yanis.
Le but est double.
D'un côté, nous devons traiter des logs apaches afin d'en faire un fichier .json où chaque objet json de ce .json est un dictionnaire avec les champs d'un log apache.
Par exemple on retrouve l'adresse ip qui a fait la requête, le code de réponse, la taille du fichier etc.
Et d'un autre côté, nous devons, à partir du fichier json créé, déterminer les données intéressantes d'un point de vue commercial et de sécurité pour en faire des statistiques.
Le fichier fonctions.py contient toutes les fonctions nécessaires pour le découpage, la création du json et la statistique.
Le fichier main.py contient la partie exécution du fichier qui va faire appel aux fonctions de fonctions.py

Exemple d'utilisation du programme dans un terminal :
Pour connaitre les arguments et leurs fonctions :
> /Projet-Python $ python3 main.py -h

Pour faire un json à partir de logs :
> /Projet-Python $ python3 main.py -l mes_logs mon_json

Pour afficher des statistiques à partir d'un json déjà existant :
> /Projet-Python $ python3 main.py mon_json -s

NB : si aucun argument facultatif n'est précisé, alors le programme va afficher les statistiques à partir du json.
Donc :
> /Projet-Python $ python3 main.py mon_json 

Revient à :
> /Projet-Python $ python3 main.py mon_json -s

Pour afficher des statistiques sous forme de pourcentage :
> /Projet-Python $ python3 main.py mon_json -p

Pour faire un json à partir de logs et afficher les statistiques classiques à partir de ce json :
> /Projet-Python $ python3 main.py -l mes_logs mon_json -s

Pour faire un json à partir de logs et afficher les statistiques sous forme de pourcentage à partir de ce json :
> /Projet-Python $ python3 main.py -l mes_logs mon_json -p

# Autres fichiers

apache_logs est un fichier de 10 000 logs apache, ten_logs et hundred_logs sont respectivement les 10 et 100 premières logs du fichier apache_logs. logs_sabotes est un fichier avec quelques logs volontèrement sabotées afin de vérifier la rebustesse de mon programme. 
ressources.txt est un fichier texte qui contient quelques liens vers des ressources sur internet très utiles pour ce projet.
Presentation_projet_python.pptx est le fichier utilisé lors de la présentation de notre projet.
