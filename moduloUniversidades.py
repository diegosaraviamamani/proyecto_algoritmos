# Si posee link creamos otro módulo
# Si no, solo internamente
import os


def menu():
    print("""
    MODULO UNIVERSIDADES
    1. Listar Universidades
    2. Ingresar a una universidad
    3. Crear Nueva universidad
    4. Volver
    """)
    return input("Ingrese una opción: ")

def main():
    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            print("Volver")
            break
        else:
            print("Opción inválida")