import os

def main(pdi):
    def menu():
        txt = """
        {0}
        1. Mostrar Datos
        2. Asignar un trabajador
        3. Metodo Investigar
        4. Metodo Enseñar
        5. Volver
        """.format(pdi.categoria.upper())
        print(txt)
        return input("Ingrese una opción: ")

#funciones
    def mostrarDatos():
        print(pdi)

    def asignarTrabajador():
        nombre=input('Ingrese el nombre del trabajador: ')
        ci=input('Ingrese el CI del trabajador: ')
        fechadeinicio=input('Ingrese fecha de inicio de trabajador : ')
        pdi.asignarTrabajador(nombre,ci,fechadeinicio)
#menu de seleccion
    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            mostrarDatos()
        elif opcion == "2":
            asignarTrabajador()
        elif opcion == "3":
            pdi.investigar()
        elif opcion == "4":
            pdi.enseniar()
        elif opcion == "5":
            print("Volver")
            break
        else:
            print("Opción inválida")