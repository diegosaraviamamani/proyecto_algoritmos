from librerias.lista import Lista

class Departamento:
    # constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = Lista()
        self.estudiantesGrado = Lista()
        self.pdis = Lista()

    def print(self):
        return 'Estudiantes de grado:\n{0}'.format(self.estudiantesGrado)
    def trabajadoresStr(self):
        return 'Trabajadores:\n{0}'.format(self.trabajadores)
    def pdisStr(self):
        return 'PDIs:\n{0}'.format(self.pdis)

    # metodo __str__
    def __str__(self):
        return 'Departamento: {0}'.format(self.nombre)