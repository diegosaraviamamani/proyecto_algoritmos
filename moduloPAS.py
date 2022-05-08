import os
from Lista import Lista
from Pas import PAS
from moduloPersonalAdministrativoServicios import main as mmoduloPersonalAdministrativoServicios

listaPAS=Lista()

def main():
    def menu():
        print("""
        MODULO PERSONAL ADMINISTRATIVO SERVICIOS (PAS) 
        1. Listar PAS
        2. Seleccionar PAS
        3. Crear nuevo PAS
        4. Volver
        """)
        return input("Ingrese una opción: ")

#funciones
    def listarPAS():
        print('Listar PAS')
        print(listaPAS)

    def seleccionarPAS():
        print("Seleccione PAS")
        index = int(input("Ingrese el índice: "))
        return listaPAS.obtenerEn(index)

    def nuevoPAS():
        categoria=input('Ingrese Nombre Categoria: ')
        nuevoPAS=PAS(categoria)
        listaPAS.agregar(nuevoPAS)
        print("----------------------------------------------")
        print("PDI CREADO")
    

#menu de leccion de accion
    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            listarPAS()
        elif opcion == "2":
            pas = seleccionarPAS()
            if pas:
                mmoduloPersonalAdministrativoServicios(pas)
            else:
                print("NO EXISTE PAS")
        elif opcion == "3":
            nuevoPAS()
        elif opcion == "4":
            print("Volver")
            break
        else:
            print("Opción inválida")