chain = input("Entrez une chaine de charactere: ")

with open("jour03/job00/output.txt", "w") as file:
    file.write(chain)

print("Le fichier a ete cree avec succes!")