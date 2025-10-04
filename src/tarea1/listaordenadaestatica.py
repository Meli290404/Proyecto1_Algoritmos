from src.tarea1.diccionario import Diccionario

class Array:
    def __init__(self, valor_inicial=None, tamaño=None):
        if not isinstance(tamaño, int) or tamaño < 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        self.__lista = [valor_inicial] * tamaño
        self.__tamaño = tamaño

    def __getitem__(self, índice):
        return self.__lista[índice]

    def __setitem__(self, índice, valor):
        self.__lista[índice] = valor

    def __len__(self):
        return self.__tamaño

    def get_lista(self):
        return self.__lista


class ListaOrdenadaEstatica(Diccionario):
    def __init__(self, capacidad=1000):
        self.__datos = []
        self.__capacidad = capacidad

    def inserte(self, elemento: str):
        if len(self.__datos) >= self.__capacidad:
            raise OverflowError("Capacidad máxima alcanzada.")
        self.__datos.append(elemento)
        self.__datos.sort()

    def borre(self, elemento: str):
        if elemento in self.__datos:
            self.__datos.remove(elemento)

    def limpie(self):
        self.__datos.clear()

    def miembro(self, elemento: str) -> bool:
        return elemento in self.__datos

    def imprima(self):
        print(" -> ".join(self.__datos))

    def done(self):
        self.__datos = []
        self.__capacidad = 0

    def __str__(self) -> str:
        return "[" + ", ".join(self.__datos) + "]"
