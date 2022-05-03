from persona import Persona

class Trabajador(Persona):
    def __init__(self):
        super().__init__()
        self._fechaInicio = input('Ingrese la fecha de inicio: ')
    def __str__(self):
        return '\nTRABAJADOR' + super().__str__() + '\nFecha de Inicio: ' + self._fechaInicio