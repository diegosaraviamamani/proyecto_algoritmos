from estudiante import Estudiante

class EstudianteDoctorado(Estudiante):
    # constructor
    def __init__(self, nombre, ci, universidad, programa):
        super().__init__(nombre, ci, universidad)
        self.programa = programa

    def realizarTesis(self):
        print("Realizar tesis...")

    def __str__(self) -> str:
        return '{}\nPrograma: {}'.format(super().__str__(),self.programa)