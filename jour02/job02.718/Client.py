from Personne import Personne

class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection_livres = {}

    def louer(self, bibliotheque, titre):
        if titre in bibliotheque.catalogue and bibliotheque.catalogue[titre] > 0:
            bibliotheque.catalogue[titre] -= 1
            if titre in self.collection_livres:
                self.collection_livres[titre] += 1
            else:
                self.collection_livres[titre] = 1
            print(f"{self.nom} {self.prenom} a loué le livre {titre}")
        else:
            print(f"Le livre {titre} n'est pas disponible dans la bibliothèque")