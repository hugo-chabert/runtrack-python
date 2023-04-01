from Auteur import Auteur

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        if titre in auteur.oeuvre:
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
            print(f"{quantite} exemplaire(s) du livre \"{titre}\" de l'auteur {auteur.prenom} ont été ajouté(s) au catalogue de la bibliothèque.")
        else:
            print(f"L'auteur {auteur.prenom} {auteur.nom} n'a pas écrit le livre {titre}")

    def inventaire(self, bibliotheque):
        print(" ")
        print (f"Il y a dans le catalogue {bibliotheque.nom} :" )
        for titre, quantite in self.catalogue.items():
            print(f"{titre} : {quantite}")

    def rendreLivre(self, client):
        for titre, quantite in client.collection_livres.items():
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
        client.collection_livres.clear()
        print(f"{client.nom} {client.prenom} a rendu tous ses livres du catalogue")