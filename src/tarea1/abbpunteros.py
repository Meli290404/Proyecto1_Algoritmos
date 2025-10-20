from tarea1.diccionario import Diccionario


class NodoABB:
    """Nodo de un Árbol Binario de Búsqueda (ABB)."""

    def __init__(self, elemento: str):
        self.elemento = elemento
        self.izquierdo: NodoABB | None = None
        self.derecho: NodoABB | None = None


class ABBPunteros(Diccionario):
    """Implementación del Diccionario mediante un Árbol Binario de Búsqueda (ABB) con punteros."""

    def __init__(self):
        self.__raiz: NodoABB | None = None

    # Inserción
    
    def inserte(self, elemento: str) -> None:
        """Inserta un elemento en el ABB manteniendo el orden."""
        self.__raiz = self.__insertar_rec(self.__raiz, elemento)

    def __insertar_rec(self, nodo: NodoABB | None, elemento: str) -> NodoABB:
        if nodo is None:
            return NodoABB(elemento)
        if elemento < nodo.elemento:
            nodo.izquierdo = self.__insertar_rec(nodo.izquierdo, elemento)
        else:
            nodo.derecho = self.__insertar_rec(nodo.derecho, elemento)
        return nodo

    # Borrado
    def borre(self, elemento: str) -> bool:
        """Borra un elemento del ABB. Devuelve True si existía."""
        self.__raiz, borrado = self.__borrar_rec(self.__raiz, elemento)
        return borrado

    def __borrar_rec(self, nodo: NodoABB | None, elemento: str):
        if nodo is None:
            return nodo, False

        if elemento < nodo.elemento:
            nodo.izquierdo, borrado = self.__borrar_rec(nodo.izquierdo, elemento)
        elif elemento > nodo.elemento:
            nodo.derecho, borrado = self.__borrar_rec(nodo.derecho, elemento)
        else:
            # Nodo encontrado
            if nodo.izquierdo is None:
                return nodo.derecho, True
            elif nodo.derecho is None:
                return nodo.izquierdo, True
            else:
                # Dos hijos: reemplazar con el sucesor
                sucesor = self.__minimo(nodo.derecho)
                nodo.elemento = sucesor.elemento
                nodo.derecho, _ = self.__borrar_rec(nodo.derecho, sucesor.elemento)
                return nodo, True
        return nodo, borrado

    def __minimo(self, nodo: NodoABB) -> NodoABB:
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo
    
    # Miembro
    def miembro(self, elemento: str) -> bool:
        """Devuelve True si el elemento está en el ABB."""
        return self.__miembro_rec(self.__raiz, elemento)

    def __miembro_rec(self, nodo: NodoABB | None, elemento: str) -> bool:
        if nodo is None:
            return False
        if elemento == nodo.elemento:
            return True
        if elemento < nodo.elemento:
            return self.__miembro_rec(nodo.izquierdo, elemento)
        else:
            return self.__miembro_rec(nodo.derecho, elemento)


    def limpie(self) -> None:
        """Elimina todos los elementos del ABB."""
        self.__raiz = None

    # Imprimir (in-orden)

    def imprima(self) -> None:
        """Imprime los elementos del ABB en orden (in-order)."""
        elementos: list[str] = []
        self.__in_orden(self.__raiz, elementos)
        if elementos:
            print(" -> ".join(elementos))
        else:
            print("(ABB vacío)")

    def __in_orden(self, nodo: NodoABB | None, elementos: list[str]) -> None:
        if nodo is not None:
            self.__in_orden(nodo.izquierdo, elementos)
            elementos.append(nodo.elemento)
            self.__in_orden(nodo.derecho, elementos)

    # Done (liberar estructura)

    def done(self) -> None:
        """Destruye el árbol (elimina la raíz)."""
        self.__raiz = None

    # Representación en cadena
    def __str__(self) -> str:
        elementos: list[str] = []
        self.__str_rec(self.__raiz, elementos)
        return "[" + ", ".join(elementos) + "]"

    def __str_rec(self, nodo: NodoABB | None, elementos: list[str]) -> None:
        if nodo is not None:
            self.__str_rec(nodo.izquierdo, elementos)
            elementos.append(nodo.elemento)
            self.__str_rec(nodo.derecho, elementos)
