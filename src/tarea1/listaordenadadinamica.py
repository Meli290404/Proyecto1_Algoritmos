from tarea1.diccionario import Diccionario

class Nodo:
    def __init__(self, elemento: str = ''):
        self.elemento = elemento
        self.siguiente: Nodo | None = None

class ListaOrdenadaDinamica(Diccionario):
    def __init__(self):
        self.__cabeza = Nodo()
        self.__tamaño = 0

    def __len__(self):
        return self.__tamaño

    def inserte(self, elemento: str):
        referencia: Nodo = self.__cabeza
        nodo = Nodo(elemento)

        while referencia.siguiente is not None and referencia.siguiente.elemento < elemento:
            referencia = referencia.siguiente

        nodo.siguiente = referencia.siguiente
        referencia.siguiente = nodo
        self.__tamaño += 1

    def borre(self, elemento: str) -> bool:
        referencia: Nodo = self.__cabeza
        while referencia.siguiente is not None and referencia.siguiente.elemento != elemento:
            referencia = referencia.siguiente
        if referencia.siguiente is not None:
            referencia.siguiente = referencia.siguiente.siguiente
            self.__tamaño -= 1
            return True
        return False

    def limpie(self):
        self.__cabeza.siguiente = None
        self.__tamaño = 0

    def miembro(self, elemento: str) -> bool:
        referencia: Nodo = self.__cabeza.siguiente
        while referencia is not None:
            if referencia.elemento == elemento:
                return True
            referencia = referencia.siguiente
        return False

    def imprima(self):
        referencia: Nodo = self.__cabeza.siguiente
        elementos = []
        while referencia is not None:
            elementos.append(referencia.elemento)
            referencia = referencia.siguiente
        print(" -> ".join(elementos))

    def done(self):
        self.__cabeza = None
        self.__tamaño = 0

    def __str__(self) -> str:
        referencia: Nodo = self.__cabeza.siguiente
        elementos = []
        while referencia is not None:
            elementos.append(referencia.elemento)
            referencia = referencia.siguiente
        return "[" + ", ".join(elementos) + "]"
