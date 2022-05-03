# personal de adminitracion y servicios
from trabajador import Trabajador
class PAS(Trabajador):
    # constructor
    def __init__(self):
        super().__init__()
        self._puesto=input('Ingrese el puesto: ')
    #metodo adminitrar
    def administrar(self):
        print('administrando...')
    #metodo __str__
    def __str__(self):
        return super().__str__() + '\nPuesto: {}'.format(self._puesto)

pas=PAS()
print(pas)
