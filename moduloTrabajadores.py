# Si posee link creamos otro módulo
# Si no, solo internamente
import os


def menu():
    print("""
    MODULO TRABAJADORES
    1. Ingresa a Modulo PDI
    2. Ingresa a Modulo PAS
    3. Volver
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
            print("Volver")
            break
        else:
            print("Opción inválida")