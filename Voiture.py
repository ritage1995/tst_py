class Voiture:
  
  #constructeur
  #prix est un attribut privé c est pr ça on a mettre __
  def __init__(self):
    self.name = ""
    self.couleur = ""
    self.__prix = ""

  #getter and property for delete () when we want call the getX
  @property
  def getPrix(self):
    return self.__prix

  #setter
  def setPrix(self,prix):
    slef.__prix = prix

