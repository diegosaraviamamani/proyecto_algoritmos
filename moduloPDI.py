import os
from Lista import Lista
from Pdi import PDI
from moduloPersonalDocenteInvestigador import main as moduloPersonalDocenteInvestigador

listaPDI=Lista()

def main():
    def menu():
        print("""
        MODULO PERSONAL DOCENTE INVESTIGADOR (PDI) 
        1. Listar PDI 
        2. Seleccionar PDI
        3. Crear nuevo PDI
        4. Volver
        """)
        return input("Ingrese una opción: ")

#funciones
    def listarPDI():
        print('Listar PDI')
        print(listaPDI)

    def seleccionarPDI():
        print("Seleccione PDI")
        index = int(input("Ingrese el índice: "))
        return listaPDI.obtenerEn(index)

    def nuevoPDI():
        categoria=input('Ingrese Nombre Categoria: ')
        nuevoPDI=PDI(categoria)
        listaPDI.agregar(nuevoPDI)
        print("----------------------------------------------")
        print("PDI CREADO")
    

#menu de leccion de accion
    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            listarPDI()
        elif opcion == "2":
            pdi = seleccionarPDI()
            if pdi:
                moduloPersonalDocenteInvestigador(pdi)
            else:
                print("NO EXISTE PDI")
        elif opcion == "3":
            nuevoPDI()
        elif opcion == "4":
            print("Volver")
            break
        else:
            print("Opción inválida")