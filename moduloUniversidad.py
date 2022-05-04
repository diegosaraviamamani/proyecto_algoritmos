import os
from Lista import Lista
from Universidad import Universidad

universidades = Lista()

def mainMenu():
    print("UNIVERSIDADES")
    print("""
    1. Listar universidades
    2. Nueva universidad
    3. Salir
    """)
    return input("Ingrese una opción: ")

def listarUniversidades():
    print("Listar universidades")
    for i in range(universidades.tamanio):
        print('[{0}]'.format(i), universidades[i])
def nuevaUniversidad():
    nombre = input("Ingrese el nombre de la universidad: ")
    ciudad = input("Ingrese la ciudad de la universidad: ")
    universidad = Universidad(nombre, ciudad)
    universidades.append(universidad)

def universidadMain():
    while True:
        opcion = mainMenu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            listarUniversidades()
        elif opcion == "2":
            nuevaUniversidad()
        elif opcion == "3":
            print("Salir")
            break