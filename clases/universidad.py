from departamento import Departamento
from librerias.lista import Lista

class Universidad:
    # constructor
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.trabajadores = Lista() 
        self.estudiantes = Lista()
        self.departamentos = Lista() # composicion (Departamento)

    def agregarTrabajador(self, trabajador):
        self.trabajador.agregar(trabajador)
    def agregarEstudiante(self, estudiante):
        self.estudiantes.agregar(estudiante)
    def agregarDepartamento(self, nombreDepartamento):
        departamento = Departamento(nombreDepartamento)
        self.departamentos.agregar(departamento)

    # metodo __str__
    def __str__(self):
        txt = 'Universidad: {0} - {1} '
        return txt.format(self.nombre, self.ciudad)