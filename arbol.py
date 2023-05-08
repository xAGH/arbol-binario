class Arbol:

    def __init__(self, dato):
        self.raiz = Nodo(dato)

    # Funciones privadas
    def __agregar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar(nodo.derecha, dato)

    def __inorden(self, nodo):
        if nodo is not None:
            self.__inorden(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden(nodo.derecha)

    def __preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden(nodo.izquierda)
            self.__preorden(nodo.derecha)

    def __postorden(self, nodo):
        if nodo is not None:
            self.__postorden(nodo.izquierda)
            self.__postorden(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones publicas
    def agregar(self, dato):
        self.__agregar(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
