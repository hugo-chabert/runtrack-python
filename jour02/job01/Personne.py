class Personne:
  def __init__(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom

  def SePresenter(self):
    print("Bonjour, je suis " + self.prenom, self.nom + " et je vais vous lire")
