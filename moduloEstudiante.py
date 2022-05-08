import os
from Universidad import Universidad 

#principal
def main(estudiante):
    #menu
    def menu():
        txt ="""
        {0}
        1. Mostrar datos de Estudiante
        2. Asignar una Universidad
        3. Volver
        """.format(estudiante.nombre.upper())
        print(txt)
        return input("Ingrese una opción: ")

    #funcion
    def mostrarDatos():
        print(estudiante)
    def asignarUniversidad():
        nombre=input('Ingrese el Nombre de la Universidad: ')
        ciudad=input('ingrese la ciudad de la _Universidad: ')
        universidad=Universidad(nombre, ciudad)
        estudiante.asignarUniversidad(universidad)

     

    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
           mostrarDatos()
        elif opcion == "2":
            asignarUniversidad()
        elif opcion == "3":
            print("Volver")
            break
        else:
            print("Opción inválida")

