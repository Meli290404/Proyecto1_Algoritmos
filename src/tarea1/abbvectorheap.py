from tarea1.diccionario import Diccionario


class ABBVectorHeap(Diccionario):
    """Implementación de ABB almacenado en un vector tipo heap (arreglo lineal)."""

    def __init__(self, capacidad_inicial: int = 100):
        self.__vector: list[str | None] = [None] * capacidad_inicial
        self.__capacidad = capacidad_inicial
        self.__tamaño = 0

    # ---------Inserción---------
    def inserte(self, elemento: str) -> None:
        """Inserta un elemento en el ABB representado en arreglo."""
        if self.__tamaño == 0:
            self.__vector[0] = elemento
            self.__tamaño += 1
            return

        i = 0
        while True:
            if i >= self.__capacidad:
                self.__aumentar_capacidad()
            if self.__vector[i] is None:
                self.__vector[i] = elemento
                self.__tamaño += 1
                return
            if elemento < self.__vector[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

    def __aumentar_capacidad(self):
        """Duplica la capacidad del arreglo."""
        self.__vector.extend([None] * self.__capacidad)
        self.__capacidad *= 2

    # ---------Miembro---------
    def miembro(self, elemento: str) -> bool:
        """Devuelve True si el elemento existe en el ABB."""
        i = 0
        while i < self.__capacidad and self.__vector[i] is not None:
            if elemento == self.__vector[i]:
                return True
            elif elemento < self.__vector[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2
        return False

    # ---------Borrado---------
    def borre(self, elemento: str) -> bool:
        """Borra un elemento del ABB reorganizando subárboles según las reglas del ABB."""
        return self.__borrar_rec(0, elemento)

    def __borrar_rec(self, i: int, elemento: str) -> bool:
        """Versión recursiva del borrado."""
        if i >= self.__capacidad or self.__vector[i] is None:
            return False

        if elemento < self.__vector[i]:
            return self.__borrar_rec(2 * i + 1, elemento)
        elif elemento > self.__vector[i]:
            return self.__borrar_rec(2 * i + 2, elemento)
        else:
            izq, der = 2 * i + 1, 2 * i + 2
            izq_existe = izq < self.__capacidad and self.__vector[izq] is not None
            der_existe = der < self.__capacidad and self.__vector[der] is not None

            # Sin hijos
            if not izq_existe and not der_existe:
                self.__vector[i] = None
                self.__tamaño -= 1
                return True

            # Un hijo
            if izq_existe and not der_existe:
                self.__mover_subarbol(izq, i)
                return True
            elif der_existe and not izq_existe:
                self.__mover_subarbol(der, i)
                return True

            # Dos hijos
            sucesor_idx = self.__minimo(der)
            self.__vector[i] = self.__vector[sucesor_idx]
            return self.__borrar_rec(sucesor_idx, self.__vector[i])

    def __minimo(self, i: int) -> int:
        """Devuelve el índice del nodo más a la izquierda (mínimo) desde i."""
        while i < self.__capacidad and self.__vector[2 * i + 1] is not None:
            i = 2 * i + 1
        return i

    def __mover_subarbol(self, origen: int, destino: int):
        """Copia el subárbol desde 'origen' hacia 'destino'."""
        if origen >= self.__capacidad or self.__vector[origen] is None:
            self.__vector[destino] = None
            return

        self.__vector[destino] = self.__vector[origen]
        self.__mover_subarbol(2 * origen + 1, 2 * destino + 1)
        self.__mover_subarbol(2 * origen + 2, 2 * destino + 2)

    # ---------Limpiar---------
    def limpie(self) -> None:
        """Vacía completamente el ABB."""
        self.__vector = [None] * self.__capacidad
        self.__tamaño = 0

    # ---------Imprimir---------
    def imprima(self) -> None:
        """Imprime los elementos en orden in-order."""
        elementos = []
        self.__inorden(0, elementos)
        if elementos:
            print(" -> ".join(elementos))
        else:
            print("(ABB vacío)")

    def __inorden(self, i: int, elementos: list[str]) -> None:
        if i < self.__capacidad and self.__vector[i] is not None:
            self.__inorden(2 * i + 1, elementos)
            elementos.append(self.__vector[i])
            self.__inorden(2 * i + 2, elementos)

    # ---------Done---------
    def done(self) -> None:
        """Libera la estructura."""
        self.__vector = []
        self.__capacidad = 0
        self.__tamaño = 0

    # ---------Representación---------
    def __str__(self) -> str:
        elementos = [x for x in self.__vector if x is not None]
        return "[" + ", ".join(elementos) + "]"
