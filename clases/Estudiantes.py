from Universidad import Universidad
from Persona import Persona

class Estudiante(Persona):
    #constructor
    def __init__(self, nombre, ci, universidad):
      super().__init__('',ci)
      self._nombre = nombre
      self.universidad = universidad # asociacion

    #metodo __str__
    def __str__(self):
      txt = 'Nombre: {}\nCI: {}\n{}'
      return txt.format(self._nombre, self.ci, self.universidad)