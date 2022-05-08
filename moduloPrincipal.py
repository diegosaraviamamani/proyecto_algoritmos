# Si posee link creamos otro módulo
# Si no, solo internamente
import os
from moduloUniversidades import main as moduloUniversidades
from moduloEstudiantes import main as moduloEstudiantes
from moduloTrabajadores import main as moduloTrabajadores

# Menu de opciónes

# Principal
def main():
    def menu():
        print("""
        SISTEMA EDUCATIVO UNIVERSITARIO
        1. Universidades
        2. Estudiantes
        3. Trabajadores
        4. Salir
        """)
        return input("Ingrese una opción: ")

    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            moduloUniversidades()
        elif opcion == "2":
            moduloEstudiantes()
        elif opcion == "3":
            moduloTrabajadores()
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Opción inválida")

main()