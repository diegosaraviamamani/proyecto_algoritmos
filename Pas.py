# personal de adminitracion y servicios
from Trabajador import Trabajador

class PAS:
    # constructor
    def __init__(self, puesto):
        self.puesto = puesto
        self.trabajador = None # composicion (Trabajador)

    def asignarTrabajador(self, nombre, ci, fechaInicio):
        self.trabajador = Trabajador(nombre, ci, fechaInicio)

    def administrar(self):
        print('Administrando...')

    # metodo __str__
    def __str__(self):
        txt = 'Puesto: {0} - {1}'
        return txt.format(self.puesto, self.trabajador if self.trabajador else 'No se asigno un trabajador')

# pas = PAS('Administrador', 'Juan', '12345678', '01/01/2000')
# print(pas)