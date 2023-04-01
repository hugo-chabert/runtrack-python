class Personne:
  def __init__(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom

  def SePresenter(self):
    print(self.prenom, self.nom)

person1 = Personne("Doe", "John")

person1.SePresenter()