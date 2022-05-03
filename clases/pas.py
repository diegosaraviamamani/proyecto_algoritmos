# personal de adminitracion y servicios
from trabajador import Trabajador

class PAS:
    # constructor
    def __init__(self, puesto, nombre, ci, fechaInicio):
        self.puesto = puesto
        self.trabajador = Trabajador(nombre, ci, fechaInicio) # composicion (Trabajador)

    def administrar(self):
        print('Administrando...')

    # metodo __str__
    def __str__(self):
        txt = 'Puesto: {0} - {1}'
        return txt.format(self.puesto, self.trabajador)

# pas = PAS('Administrador', 'Juan', '12345678', '01/01/2000')
# print(pas)