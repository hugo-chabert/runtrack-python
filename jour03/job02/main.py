import re

# Demander à l'utilisateur de saisir un nombre entier
size = int(input("Entrez la taille des mots à chercher : "))

# Ouvrir le fichier en mode lecture
with open("jour03/data.txt", "r") as file:
    # Lire le contenu du fichier
    content = file.read()

    # Compter le nombre de mots de la taille donnée
    word_count = len([word for word in re.findall(r'\b\w+\b', content) if len(word) == size])

    # Afficher le résultat
    print(f"Le fichier contient {word_count} mots de taille {size}.")