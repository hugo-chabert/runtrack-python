from Livre import Livre
from Personne import Personne

class Auteur(Personne):
    def __init__(self, nom:str, prenom:str, oeuvre: list=[]):
        super().__init__(nom, prenom)
        self.oeuvre = oeuvre

    def listerOeuvre(self):
        for livre in self.oeuvre:
            print(livre.print)

    def ecrireUnLivre(self, titre:str):
        self.oeuvre.append(Livre(titre, self))