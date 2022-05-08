from Persona import Persona

class Estudiante(Persona):
    #constructor
    def __init__(self, nombre, ci, universidad = None):
        super().__init__('',ci)
        self._nombre = nombre
        self.universidad = universidad # asociacion

    def asignarUniversidad(self, universidad):
        self.universidad = universidad

    #metodo __str__
    def __str__(self):
        txt = 'Nombre: {}\nCI: {}\n{}'
        return txt.format(self._nombre, self.ci, self.universidad if self.universidad!=None else 'No tiene universidad')