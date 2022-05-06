import os
from Lista import Lista
from moduloUniversidad import universidadMain

universidades = Lista()

# Menu Principal
def main_menu():
    print("""
SISTEMA EDUCATIVO UNIVERSITARIO
    1. Universidades
    2. Estudiantes
    3. Trabajadores
    4. Salir
    """)
    return input("Ingrese una opción: ")

def main():
    while True:
        opcion = main_menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            universidadMain()
        elif opcion == "2":
            print("Estudiantes")
        elif opcion == "3":
            print("Trabajadores")
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Opción inválida")
main()

def ingresar_sistema():
    print("Ingresar al sistema")