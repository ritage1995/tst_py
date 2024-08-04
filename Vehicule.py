# we want this class be abstract 
#we will import ABC from abc

from abc import ABC, abstractmethod
class Vehicule(ABC):
  
  def __init__(self):
    self.type = ""
    self.marque = ""
    sef.couleur = ""
    self.__prix = ""

  def setPrix(sef,prix):
    self.__prix = prix
    
  def setType(sef,type):
    self.type = type

  def getType(self):
    return self.type
  
  def getPrix(self):
    return self.__prix

  @abstractmethod
  def consommation():
    pass
