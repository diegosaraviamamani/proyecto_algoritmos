import os

def main(pas):
    def menu():
        txt = """
        {0}
        1. Mostrar Datos
        2. Asignar un trabajador
        3. Metodo administrar
        4. Volver
        """.format(pas.puesto.upper())
        print(txt)
        return input("Ingrese una opción: ")

#funciones
    def mostrarDatos():
        print(pas)
    def asignarTrabajador():
        nombre=input('Ingrese el nombre del trabajador: ')
        ci=input('Ingrese el CI del trabajador: ')
        fechadeinicio=input('Ingrese fecha de inicio de trabajador : ')
        pas.asignarTrabajador(nombre,ci,fechadeinicio)

#menu de seleccion
    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            mostrarDatos()
        elif opcion == "2":
            pas.administrar()
        elif opcion == "3":
            asignarTrabajador()
        elif opcion == "4":
            print("Volver")
            break
        else:
            print("Opción inválida")