# Si posee link creamos otro módulo
# Si no, solo internamente
import os
from moduloPDI import main as moduloPDI
from moduloPAS import main as moduloPAS


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
            moduloPDI()
        elif opcion == "2":
            moduloPAS()
        elif opcion == "3":
            print("Volver")
            break
        else:
            print("Opción inválida")