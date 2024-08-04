# from fichier Vehicule import class Vehicule ou bien on fait * signifier tt
from Vehicule import Vehicule

class Voiture(Vehicule):
  
  #constructeur
  def __init__(self):
    self.__A = ""

  #getter and property for delete () when we want call the getX
  @property
  def getA(self):
    return self.__A

  #setter
  def setA(self,A):
    slef.__A = A

  def consommation(self):
    return Vehicule.motor * 2
