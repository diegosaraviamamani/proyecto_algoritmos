from Departamento import Departamento
from Lista import Lista

class Universidad:
    # constructor
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.trabajadores = Lista() 
        self.estudiantes = Lista()
        self.departamentos = Lista() # composicion (Departamento)

    def agregarTrabajador(self, trabajador):
        self.trabajadores.agregar(trabajador)
    def agregarEstudiante(self, estudiante):
        self.estudiantes.agregar(estudiante)
        
    def agregarDepartamento(self, nombreDepartamento):
        departamento = Departamento(nombreDepartamento)
        self.departamentos.agregar(departamento)

    # metodo __str__
    def __str__(self):
        txt = 'Universidad: {0} - {1} '
        return txt.format(self.nombre, self.ciudad)

uni = Universidad('UCA', 'Bogota')
uni.agregarDepartamento('Informatica')
uni.agregarDepartamento('Filosofia')

print(uni)

print(uni.departamentos)