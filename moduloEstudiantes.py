import os
from Lista import Lista
from Estudiante import Estudiante
from moduloEstudiante import main as moduloEstudiante

listaEstudiantes=Lista()


def main():
    def menu():
        print("""
        MODULO ESTUDIANTES
        1. Listar Estudiantes
        2. Seleccionar un estudiante
        3. Crear nuevo estudiante
        4. Volver
        """)
        return input("Ingrese una opción: ")
#funcion 
    def listarEstudiantes():
        print('Listar Estudiantes')
        print(listaEstudiantes)
    def seleccionarEstudiante():
        print("Seleccione una Estudiante")
        index = int(input("Ingrese el índice: "))
        return listaEstudiantes.obtenerEn(index)


    
    def nuevoEstudiante():
        nombre=input('INGRESE NOMBRE DE ESTUDIANTE: ')
        ci=input('INGRESE LA CI DEL ESTUDIANTE:')
        nuevoEstudiante=Estudiante(nombre, ci )
        listaEstudiantes.agregar(nuevoEstudiante)
        print("-----------------------------------------------------")
        print("ESTUDIANTE  CREADA")


# menu seleccion de accion 
    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            listarEstudiantes()
        elif opcion == "2":
            estudiante = seleccionarEstudiante()
            if estudiante:
                moduloEstudiante(estudiante)
            else:
                print("NO EXISTE LA ESTUDIANTE")
        elif opcion == "3":
            nuevoEstudiante()
        elif opcion == "4":
            print("Volver")
            break
        else:
            print("Opción inválida")