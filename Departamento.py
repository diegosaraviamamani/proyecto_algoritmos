from Lista import Lista

class Departamento:
    # constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = Lista() #agregación
        self.estudiantesGrado = Lista() #agregación
        self.pdis = Lista()
    
    def agregarTrabajador(self, trabajador):
        self.trabajadores.agregar(trabajador)
    def agregarEstudianteGrado(self, estudiante):
        self.estudiantesGrado.agregar(estudiante)
    def agregarPDI(self, pdi):
        self.pdis.agregar(pdi)

    # metodo __str__
    def __str__(self):
        return 'Departamento: {0}'.format(self.nombre)
