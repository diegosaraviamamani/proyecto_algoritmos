#perosnal docente e investigador
from Trabajador import Trabajador

class PDI:
    # constructor
    def __init__(self, categoria, nombre, ci, fechaInicio):
        self.categoria = categoria
        self.trabajador = Trabajador(nombre, ci, fechaInicio) # composicion (Trabajador)

    def investigar(self):
        print('investigando...')
    def enseniar(self):
        print('enseñando...')

    # metodo __str__
    def __str__(self):
        txt = 'Puesto: {0} - {1}'
        return txt.format(self.puesto, self.trabajador)

# pdi = PDI('Docente II', 'Juan', '12345678', '01/01/2000')
# print(pdi) 