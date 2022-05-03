from estudiante import Estudiante

class EstudianteDoctorado(Estudiante):
    def __init__(self):
        super().__init__()
        self.__programa=input("Ingrese programa: ")
    def __str__(self) -> str:
        return super().__str__() + "\nPrograma: " + self.__programa
    def RealizarTesis(self):
        print("Realizar tesis")

estudianteDoctorado = EstudianteDoctorado()
print(estudianteDoctorado)
