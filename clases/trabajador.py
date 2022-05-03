from persona import Persona

class Trabajador(Persona):
    def __init__(self, nombre, ci, fechaInicio):
        super().__init__(nombre, ci)
        self.fechaInicio = fechaInicio

    def __str__(self):
        txt = '{} - Fecha de inicio: {}'
        return txt.format(super().__str__(), self.fechaInicio)