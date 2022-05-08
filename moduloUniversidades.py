import os
from Lista import Lista
from Universidad import Universidad
from moduloUniversidad import main as moduloUniversidad

listaUniversidades =Lista()

# Principal
def main():
    # Menu de opciónes
    def menu():
        print("""
        MODULO UNIVERSIDADES
        1. Mostrar Universidades
        2. Ingresar a una universidad
        3. Crear Nueva universidad
        4. Volver
        """)
        return input("Ingrese una opción: ")

    # Funciones
    def mostrarUniversidades():
        print("Lista de Universidades")
        print(listaUniversidades)

    def seleccionarUniversidad():
        print("Seleccione una universidad")
        index = int(input("Ingrese el índice: "))
        return listaUniversidades.obtenerEn(index)

    def nuevaUniversidad():
        nombre = input("Ingrese el nombre de la universidad: ")
        ciudad = input("Ingrese la ciudad de la universidad: ")
        nuevaUniversidad = Universidad(nombre, ciudad)
        listaUniversidades.agregar(nuevaUniversidad)
        print("-----------------------------------------------------")
        print("UNIVERSIDAD CREADA")

    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            mostrarUniversidades()
        elif opcion == "2":
            universidad = seleccionarUniversidad()
            if universidad:
                moduloUniversidad(universidad)
            else:
                print("NO EXISTE LA UNIVERSIDAD")
        elif opcion == "3":
            nuevaUniversidad()
        elif opcion == "4":
            print("Volver")
            break
        else:
            print("Opción inválida")