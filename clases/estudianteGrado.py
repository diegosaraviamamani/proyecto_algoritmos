from estudiante import Estudiante

class EstudianteGrado(Estudiante):
    # constructor
    def __init__(self, nombre, ci, universidad, titulacion):
        super().__init__(nombre, ci, universidad)
        self._titulacion = titulacion

    def colaboracion(self):
        print('colaborar....')

    # metodo __str__
    def __str__(self):
        return '{} \nTitulacion: {}'.format(super().__str__(),self._titulacion)