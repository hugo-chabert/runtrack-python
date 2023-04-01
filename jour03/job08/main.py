import matplotlib.pyplot as plt

# Initialiser un dictionnaire pour stocker les comptages de lettres
letter_counts = {}

# Ouvrir le fichier et parcourir chaque ligne
with open("jour03/data.txt", "r") as f:
    for line in f:
        # Séparer chaque mot par espace
        words = line.strip().split()
        # Parcourir chaque mot et mettre à jour le comptage pour sa première lettre
        for word in words:
            letter = word[0].lower() # Convertir en minuscule pour ne pas distinguer les majuscules et les minuscules
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

# Calculer le nombre total de mots
total_words = sum(letter_counts.values())

# Calculer le pourcentage de présence de chaque lettre en début de mot
percentages = {letter: count / total_words * 100 for letter, count in letter_counts.items()}

# Trier les lettres par ordre alphabétique
letters = sorted(percentages.keys())

# Créer un graphique à barres représentant les pourcentages
plt.bar(letters, [percentages[letter] for letter in letters])

# Définir les étiquettes des axes
plt.xlabel("Lettre en début de mot")
plt.ylabel("Pourcentage de présence")

# Afficher le graphique
plt.show()