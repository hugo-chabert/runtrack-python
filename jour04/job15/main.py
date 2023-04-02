def compare_strings(s1, s2):
    # Cas de base : les deux chaînes sont vides
    if not s1 and not s2:
        return 1
    # Cas de base : la deuxième chaîne est vide
    elif not s2:
        return 0
    # Cas où le premier caractère de la deuxième chaîne est un *
    elif s2[0] == '*':
        # Récursivement, on compare la première chaîne avec la deuxième en avançant d'un caractère dans la première chaîne ou en laissant le * vide
        return compare_strings(s1, s2[1:]) or compare_strings(s1[1:], s2)
    # Cas où les deux premiers caractères des chaînes sont identiques
    elif s1 and (s1[0] == s2[0]):
        # On continue la comparaison avec le reste des chaînes
        return compare_strings(s1[1:], s2[1:])
    # Si aucun des cas précédents ne s'applique, les chaînes ne sont pas identiques
    else:
        return 0

# Demande à l'utilisateur de fournir les deux chaînes
s1 = input("Entrez la première chaîne de caractères : ")
s2 = input("Entrez la deuxième chaîne de caractères : ")

# Compare les deux chaînes
if compare_strings(s1, s2):
    print("1")
else:
    print("0")