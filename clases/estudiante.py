from persona import Persona

class Estudiante(Persona):
    #constructor
    def __init__(self):
      super().__init__()

    #metodo __str__
    def __str__(self):
      return '\nESTUDIANTE\nNombre: {}\nCI: {}'.format(self._nombre,self._ci)