import os


def menu():
    print("""
    MODULO ESTUDIANTES
    1. Listar Estudiantes
    2. Seleccionar un estudiante
    3. Crear nuevo estudiante
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