import re

# Ouvrir le fichier en mode lecture
with open("jour03/data.txt", "r") as file:
    # Lire le contenu du fichier
    content = file.read()

    # Compter le nombre de mots
    word_count = len(re.findall(r'\b\w+\b', content))

    # Afficher le résultat
    print(f"Le fichier contient {word_count} mots.")