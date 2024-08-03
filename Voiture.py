class Voiture:
  
  #constructeur
  #prix est un attribut privé c est pr ça on a mettre __
  def __init__(self):
    self.couleur = ""
    self.__prix = ""

  #getter
  def getPrix(self):
    return self.__prix

  #setter
  def setPrix(self,prix):
    slef.__prix = prix

