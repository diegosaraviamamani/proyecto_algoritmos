from Trabajador import Trabajador


class Doctor(Trabajador):
    def __init__(self, nombre, ci, fechaInicio):
        super().__init__(nombre, ci, fechaInicio)

    def __str__(self):
        return super().__str__()