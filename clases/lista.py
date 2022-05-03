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
    def obtenerInicio(self):
        return self.nodoInicial.valor
    def obtenerFinal(self):
        return self.nodoFinal.valor
    def obtenerEn(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return None
        nodoActual = self.nodoInicial
        for i in range(posicion):
            nodoActual = nodoActual.siguienteNodo
        return nodoActual.valor
    def eliminarInicio(self):
        if self.estaVacia():
            return None
        valor = self.nodoInicial.valor
        self.nodoInicial = self.nodoInicial.siguienteNodo
        self.tamanio -= 1
        if self.estaVacia():
            self.nodoFinal = None
        return valor
    def eliminarFinal(self):
        if self.estaVacia():
            return None
        valor = self.nodoFinal.valor
        if self.tamanio == 1:
            self.nodoInicial = None
            self.nodoFinal = None
        else:
            penultimoNodo = self.nodoInicial
            while penultimoNodo.siguienteNodo != self.nodoFinal:
                penultimoNodo = penultimoNodo.siguienteNodo
            self.nodoFinal = penultimoNodo
            self.nodoFinal.siguienteNodo = None
        self.tamanio -= 1
        return valor
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
    def iterar(self, funcion):
        nodoActual = self.nodoInicial
        while nodoActual != None:
            funcion(nodoActual)
            nodoActual = nodoActual.siguienteNodo
    #metodo __str__
    def __str__(self):
        cadena = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            cadena += str(nodoActual.valor) + " "
            nodoActual = nodoActual.siguienteNodo
        return cadena