#perosnal docente e investigador
from Trabajador import Trabajador

class PDI:
    # constructor
    def __init__(self, categoria):
        self.categoria = categoria
        self.trabajador = None # composicion (Trabajador)

    def asignarTrabajador(self, nombre, ci, fechaInicio):
        self.trabajador = Trabajador(nombre, ci, fechaInicio)

    def investigar(self):
        print('investigando...') if self.trabajador else print('Aun no se asigno un trabajador')
    def enseniar(self):
        print('enseñando...') if self.trabajador else print('Aun no se asigno un trabajador')

    # metodo __str__
    def __str__(self):
        txt = 'Puesto: {0} - {1}'
        return txt.format(self.categoria, self.trabajador if self.trabajador else 'No se asigno un trabajador')

# pdi = PDI('Docente II', 'Juan', '12345678', '01/01/2000')
# print(pdi) 