#definir la clase Nodo
class Nodo:
    #constructor
    def __init__(self, valor=None, siguienteNodo=None):
        self.valor = valor
        self.siguienteNodo = siguienteNodo
    def __str__(self):
        return str(self.valor)

class Lista:
    #constructor
    def __init__(self):
        self.nodoInicial = None
        self.nodoFinal = None
        self.tamanio = 0
    #métodos
    def obtenerTamanio(self):
        return self.tamanio
    def estaVacia(self):
        return self.tamanio == 0
    def agregar(self, valor):
        nuevoNodo = Nodo(valor)
        if self.estaVacia():
            self.nodoInicial = nuevoNodo
        else:
            self.nodoFinal.siguienteNodo = nuevoNodo
        self.nodoFinal = nuevoNodo
        self.tamanio += 1

    def obtenerEn(self, indice):
        if indice < 0 or indice >= self.tamanio:
            return None
        nodoActual = self.nodoInicial
        for i in range(indice):
            nodoActual = nodoActual.siguienteNodo
        return nodoActual.valor

    def eliminarEn(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return None
        if posicion == 0:
            return self.eliminarInicio()
        if posicion == self.tamanio - 1:
            return self.eliminarFinal()
        anteriorNodo = self.nodoInicial
        for i in range(posicion - 1):
            anteriorNodo = anteriorNodo.siguienteNodo
        valor = anteriorNodo.siguienteNodo.valor
        anteriorNodo.siguienteNodo = anteriorNodo.siguienteNodo.siguienteNodo
        self.tamanio -= 1
        return valor

    def __str__(self):
        cadena = ""
        nodoActual = self.nodoInicial
        i = 0
        while nodoActual != None:
            cadena += '-------------------------------\n'
            cadena += '[{0}]\n'.format(i)
            cadena += str(nodoActual.valor) + "\n"
            nodoActual = nodoActual.siguienteNodo
            i += 1
        if i ==  0:
            cadena += 'No hay elementos en la lista'
        return cadena