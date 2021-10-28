# Projet-Python
Projet scolaire de python à l'IUT Réseaux et Télécommunications de l'université Nice Côte d'Azur dans le cadre du module M3206 "Automatisation des tâches d'administration.
Réalisé par JUST Maxime et KOUIDRI Yanis.
Le but est double.
D'un côté, nous devons traiter des logs apaches afin d'en faire un fichier .json où chaque objet json de ce .json est un dictionnaire avec les champs d'un log apache.
Par exemple on retrouve l'adresse ip qui a fait la requête, le code de réponse, la taille du fichier etc.
Et d'un autre côté, nous devons, à partir du fichier json créé, déterminer les données intéressantes d'un point de vue commercial et de sécurité pour en faire des statistiques.
Le fichier fonctions.py contient toutes les fonctions nécessaires pour le découpage, la création du json et la statistique.
Le fichier main.py contient la partie exécution du fichier qui va faire appel aux fonctions de fonctions.py

