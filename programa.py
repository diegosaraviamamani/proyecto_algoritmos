import os
from clases.librerias.lista import Lista
from modulo_universidad import universidad_main

universidades = Lista()

# Menu Principal
def main_menu():
    print("""
SISTEMA EDUCATIVO UNIVERSITARIO
    1. Ingresar al sistema
    2. Salir
    """)
    return input("Ingrese una opción: ")

def main():
    while True:
      opcion = main_menu()
      os.system('cls') | os.system('clear')
      if opcion == "1":
          universidad_main
      elif opcion == "2":
          print("Salir")
          break
      else:
          print("Opción inválida")
main()

def ingresar_sistema():
    print("Ingresar al sistema")