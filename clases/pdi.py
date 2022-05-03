#perosnal docente e investigador
from trabajador import Trabajador

class PDI(Trabajador):
    #contructor
    def __init__(self):
        super().__init__()
        self._categoria=input('Ingrese la categoria: ')

    #metodos
    def investigar(self):
        print('investigando...')
    def enseniar(self):
        print('enseñando...')
        
    #metodo __str__
    def __str__(self):
        return super().__str__()+ '\ncategoria: {}'.format(self._categoria)

pdi = PDI()
print(pdi)