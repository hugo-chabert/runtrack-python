import matplotlib.pyplot as plt

# Initialiser un dictionnaire pour stocker les comptages de taille de mot
word_counts = {}

# Ouvrir le fichier et parcourir chaque ligne
with open("jour03/data.txt", "r") as f:
    for line in f:
        # Séparer chaque mot par espace
        words = line.strip().split()
        # Parcourir chaque mot et mettre à jour le comptage pour sa taille
        for word in words:
            length = len(word)
            if length in word_counts:
                word_counts[length] += 1
            else:
                word_counts[length] = 1

# Calculer le nombre total de mots
total_words = sum(word_counts.values())

# Calculer le pourcentage d'apparition de chaque taille de mot
percentages = {length: count / total_words * 100 for length, count in word_counts.items()}

# Trier les tailles de mots par ordre croissant
lengths = sorted(percentages.keys())

# Créer un graphique à barres représentant les pourcentages
plt.bar(lengths, [percentages[length] for length in lengths])

# Définir les étiquettes des axes
plt.xlabel("Taille des mots")
plt.ylabel("Pourcentage d'apparition")

# Afficher le graphique
plt.show()


