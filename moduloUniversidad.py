import imp
import os
from Estudiante import Estudiante
from Trabajador import Trabajador
from moduloEstudiantes import listaEstudiantes

# Principal
def main(universidad):
    # Menu de opciónes
    def menu():
        txt = """
        {0}
        1. Mostrar datos
        2. Listar estudiantes
        3. Agregar estudiante
        4. Listar trabajadores
        5. Agregar trabajador
        6. Listar departamentos
        7. Agregar departamento
        8. Volver
        """.format(universidad.nombre.upper())
        print(txt)
        return input("Ingrese una opción: ")

    # Funciones
    def mostrarDatos():
        print(universidad)
    def listarEstudiantes():
        print("Lista de estudiantes")
        print(universidad.estudiantes)
    def agregarEstudiante():
        nombre = input("Ingrese el nombre completo del estudiante: ")
        ci = input("Ingrese el ci del estudiante: ")
        estudiante = Estudiante(nombre, ci, universidad)
        listaEstudiantes.agregar(estudiante)
        universidad.agregarEstudiante(estudiante)
        print("-----------------------------------------------------")
        print("ESTUDIANTE CREADO")

    def listarTrabajadores():
        print("Lista de trabajadores")
        print(universidad.trabajadores)
    def agregarTrabajador():
        nombre = input("Ingrese el nombre completo del trabajador: ")
        ci = input("Ingrese el ci del trabajador: ")
        fechaInicio = input("Ingrese la fecha de inicio del trabajador: ")
        trabajador = Trabajador(nombre, ci, fechaInicio)
        universidad.agregarTrabajador(trabajador)
        print("-----------------------------------------------------")
        print("TRABAJADOR CREADO")
    
    def listarDepartamentos():
        print("Lista de departamentos")
        print(universidad.departamentos)
    def agregarDepartamento():
        nombreDepartamento = input("Ingrese el nombre del departamento: ")
        universidad.agregarDepartamento(nombreDepartamento)
        print("-----------------------------------------------------")
        print("DEPARTAMENTO CREADO")

    while True:
        opcion = menu()
        os.system('cls') | os.system('clear')
        if opcion == "1":
            mostrarDatos()
        elif opcion == "2":
            listarEstudiantes()
        elif opcion == "3":
            agregarEstudiante()
        elif opcion == "4":
            listarTrabajadores()
        elif opcion == "5":
            agregarTrabajador()
        elif opcion == "6":
            listarDepartamentos()
        elif opcion == "7":
            agregarDepartamento()
        elif opcion == "8":
            print("Volver")
            break
        else:
            print("Opción inválida")