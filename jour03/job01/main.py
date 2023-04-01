import re

# Expression régulière pour détecter les extensions de domaine
pattern = re.compile(r"(\.\w+)")

# Ouverture du fichier et lecture du contenu
with open("jour03/jour01/domains.xml", "r") as f:
    contenu = f.read()

# Recherche des extensions de domaine dans le contenu
matches = pattern.findall(contenu)

# Comptage des extensions de domaine
comptes = {}
compteur = 0
for match in matches:
    if match in comptes:
        comptes[match] += 1
        compteur += 1
    else:
        comptes[match] = 1

# Affichage du résultat
for extension, compte in comptes.items():
    print(f"{extension}: {compte} occurrence(s)")

print(compteur)