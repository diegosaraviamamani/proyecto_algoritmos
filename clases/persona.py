class Persona:
    def __init__(self):
        self._nombre = input('Ingrese el nombre: ')
        self._ci = input('Ingrese la cedula: ')
    def __str__(self):
        return '\nNombre: ' + self._nombre + '\nCI: ' + self._ci