import matplotlib.pyplot as plt

# Ouverture du fichier "data.txt"
with open("jour03/data.txt", "r") as f:
    text = f.read()

# Convertir toutes les lettres en minuscules
text = text.lower()

# Initialiser un dictionnaire vide pour stocker les occurrences de chaque lettre
occurrences = {}

# Parcourir chaque lettre dans le fichier et ajouter 1 à la valeur correspondante dans le dictionnaire
for letter in text:
    if letter.isalpha():
        occurrences[letter] = occurrences.get(letter, 0) + 1

# Calculer le pourcentage d'apparition de chaque lettre
total_letters = sum(occurrences.values())
percentages = {letter: (count / total_letters) * 100 for letter, count in occurrences.items()}

# Trier les lettres par ordre alphabétique
sorted_letters = sorted(percentages.keys())

# Créer un histogramme des pourcentages d'apparition de chaque lettre
plt.bar(range(len(sorted_letters)), [percentages[letter] for letter in sorted_letters])
plt.xticks(range(len(sorted_letters)), sorted_letters)
plt.xlabel("Lettre")
plt.ylabel("Pourcentage d'apparition")
plt.show()