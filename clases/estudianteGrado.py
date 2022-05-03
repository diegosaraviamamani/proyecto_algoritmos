from estudiante import Estudiante

class Grado(Estudiante):
    def __init__(self):
        super().__init__()
        self._titulacion=input('Ingrese Titulacion: ')
    def colaboracion(self):
        print('colaborar....')
    def __str__(self):
        return '{} \nTitulacion: {}'.format(super().__str__(),self._titulacion)

grado=Grado()
print(grado)