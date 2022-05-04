class Persona:
    def __init__(self, nombre, ci):
        self.nombre = nombre
        self.ci = ci
    def __str__(self):
        txt = 'Nombre: {0} - CI: {1}'
        return txt.format(self.nombre, self.ci)