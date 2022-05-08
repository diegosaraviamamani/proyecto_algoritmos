import os

def main(pas):
    def menu():
        txt = """
        {0}
        1. Mostrar Datos
        2. Metodo Administrar
        3. Volver
        """.format(pas.puesto.upper())
        print(txt)
        return input("Ingrese una opción: ")

#funciones
    def mostrarDatos():
        print(pas)

#menu de seleccion
    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            mostrarDatos()
        elif opcion == "2":
            pas.administrar()
        elif opcion == "3":
            print("Volver")
            break
        else:
            print("Opción inválida")