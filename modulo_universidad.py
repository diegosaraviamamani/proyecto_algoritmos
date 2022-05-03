import os
from clases.librerias.lista import Lista
from clases.universidad import Universidad

universidades = Lista()

def main_menu():
    print("UNIVERSIDADES")
    print("""
    1. Listar universidades
    2. Nueva universidad
    3. Salir
    """)
    return input("Ingrese una opción: ")

def listar_universidades():
    print("Listar universidades")
    for i in range(universidades.tamanio):
        print('[{0}]'.format(i), universidades[i])
def nueva_universidad():
    nombre = input("Ingrese el nombre de la universidad: ")
    ciudad = input("Ingrese la ciudad de la universidad: ")
    universidad = Universidad(nombre, ciudad)
    universidades.append(universidad)

def universidad_main():
    while True:
        opcion = main_menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            listar_universidades()
        elif opcion == "2":
            nueva_universidad()
        elif opcion == "3":
            print("Salir")
            break