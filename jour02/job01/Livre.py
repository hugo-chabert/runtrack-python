class Livre:
    def __init__(self, titre:str, Auteur):
        self.titre = titre
        self.auteur = Auteur

    @property
    def print(self):
        return self.titre
