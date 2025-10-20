from tarea1.diccionario import Diccionario


class NodoTrie:
    """Nodo del Trie con hijos representados por un diccionario."""
    __slots__ = ["hijos", "es_fin"]

    def __init__(self):
        self.hijos: dict[str, "NodoTrie"] = {}
        self.es_fin: bool = False


class TriePunteros(Diccionario):
    """Implementación del Trie usando nodos enlazados (punteros)."""

    def __init__(self):
        self.__raiz = NodoTrie()
        self.__tamaño = 0

    # ---------Inserción---------
    def inserte(self, palabra: str) -> None:
        """Inserta una palabra en el Trie."""
        nodo = self.__raiz
        for c in palabra:
            if c < "a" or c > "z":
                continue
            if c not in nodo.hijos:
                nodo.hijos[c] = NodoTrie()
            nodo = nodo.hijos[c]
        if not nodo.es_fin:
            nodo.es_fin = True
            self.__tamaño += 1

    # ---------Miembro---------
    def miembro(self, palabra: str) -> bool:
        """Devuelve True si la palabra existe en el Trie."""
        nodo = self.__raiz
        for c in palabra:
            if c not in nodo.hijos:
                return False
            nodo = nodo.hijos[c]
        return nodo.es_fin

    # ---------Borrado---------
    def borre(self, palabra: str) -> bool:
        """Borra una palabra del Trie. Retorna True si existía y se eliminó."""
        eliminado, _ = self.__borrar_rec(self.__raiz, palabra, 0)
        return eliminado

    def __borrar_rec(self, nodo: NodoTrie, palabra: str, nivel: int) -> tuple[bool, bool]:
        """
        Retorna (eliminado, debe_podarse).
        - eliminado: True si la palabra existía y fue eliminada.
        - debe_podarse: True si este nodo queda sin hijos y no es fin de otra palabra.
        """
        if nivel == len(palabra):
            if not nodo.es_fin:
                return False, False
            nodo.es_fin = False
            self.__tamaño -= 1
            return True, len(nodo.hijos) == 0

        c = palabra[nivel]
        if c not in nodo.hijos:
            return False, False

        eliminado, podar_hijo = self.__borrar_rec(nodo.hijos[c], palabra, nivel + 1)

        if eliminado and podar_hijo:
            del nodo.hijos[c]

        debe_podarse = (not nodo.es_fin) and len(nodo.hijos) == 0
        return eliminado, debe_podarse

    # ---------Limpiar---------
    def limpie(self) -> None:
        """Limpia el Trie completamente."""
        self.__raiz = NodoTrie()
        self.__tamaño = 0

    # ---------Imprimir---------
    def imprima(self) -> None:
        """Imprime todas las palabras almacenadas en orden alfabético."""
        palabras: list[str] = []
        self.__recorrer(self.__raiz, "", palabras)
        if palabras:
            print(" -> ".join(palabras))
        else:
            print("(Trie vacío)")

    def __recorrer(self, nodo: NodoTrie, prefijo: str, palabras: list[str]) -> None:
        if nodo.es_fin:
            palabras.append(prefijo)
        for c in sorted(nodo.hijos.keys()):
            self.__recorrer(nodo.hijos[c], prefijo + c, palabras)

    # ---------Done---------
    def done(self) -> None:
        """Libera la estructura."""
        self.__raiz = None
        self.__tamaño = 0

    # ---------Representación---------
    def __str__(self) -> str:
        palabras: list[str] = []
        if self.__raiz is not None:
            self.__recorrer(self.__raiz, "", palabras)
        return "[" + ", ".join(palabras) + "]"
