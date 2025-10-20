# -*- coding: utf-8 -*-
"""
Implementación del Diccionario mediante un Trie utilizando arreglos.
Cada nodo del Trie se representa mediante índices dentro de un arreglo.
"""

from tarea1.diccionario import Diccionario
from typing import List, Optional, Tuple


class NodoTrieArray:
    """Nodo del Trie representado por índices en arreglos."""
    __slots__ = ["hijos", "es_fin"]

    def __init__(self):
        # 26 posibles letras 'a'..'z', cada una apunta al índice del hijo o None
        self.hijos: List[Optional[int]] = [None] * 26
        self.es_fin: bool = False


class TrieArreglos(Diccionario):
    """Implementación del Trie utilizando listas de nodos (arreglos)."""

    def __init__(self):
        self.__nodos: List[NodoTrieArray] = [NodoTrieArray()]  # nodo raíz
        self.__tamaño = 0

    # ---------Inserción---------
    def inserte(self, palabra: str) -> None:
        """Inserta una palabra en el Trie."""
        actual = 0  # índice del nodo actual
        for c in palabra:
            idx = ord(c) - ord("a")
            if idx < 0 or idx >= 26:
                # ignorar caracteres fuera de 'a'..'z'
                continue
            if self.__nodos[actual].hijos[idx] is None:
                self.__nodos.append(NodoTrieArray())
                self.__nodos[actual].hijos[idx] = len(self.__nodos) - 1
            actual = self.__nodos[actual].hijos[idx]  # type: ignore[assignment]
        if not self.__nodos[actual].es_fin:
            self.__nodos[actual].es_fin = True
            self.__tamaño += 1

    # ---------Miembro---------
    def miembro(self, palabra: str) -> bool:
        """Devuelve True si la palabra está en el Trie."""
        actual = 0
        for c in palabra:
            idx = ord(c) - ord("a")
            if idx < 0 or idx >= 26:
                return False
            hijo = self.__nodos[actual].hijos[idx]
            if hijo is None:
                return False
            actual = hijo
        return self.__nodos[actual].es_fin

    # ---------Borrado---------
    def borre(self, palabra: str) -> bool:
        """Borra una palabra del Trie. True si existía y se eliminó."""
        eliminado, _ = self.__borrar_rec(0, palabra, 0)
        return eliminado

    def __borrar_rec(self, nodo_idx: int, palabra: str, nivel: int) -> Tuple[bool, bool]:
        """
        Retorna (eliminado, debe_podarse).
        - eliminado: True si la palabra existía y se desmarcó es_fin.
        - debe_podarse: True si este nodo queda sin hijos y no es fin de otra palabra.
        """
        # Caso base: llegamos al final de la palabra
        if nivel == len(palabra):
            if not self.__nodos[nodo_idx].es_fin:
                return False, False
            self.__nodos[nodo_idx].es_fin = False
            self.__tamaño -= 1
            # Podar si no tiene hijos
            return True, all(h is None for h in self.__nodos[nodo_idx].hijos)

        # Validar letra
        idx_letra = ord(palabra[nivel]) - ord("a")
        if idx_letra < 0 or idx_letra >= 26:
            # letra fuera del alfabeto permitido -> no se elimina nada
            return False, False

        hijo = self.__nodos[nodo_idx].hijos[idx_letra]
        if hijo is None:
            # camino no existe -> palabra no estaba
            return False, False

        # Borrar en el subárbol
        eliminado, podar_hijo = self.__borrar_rec(hijo, palabra, nivel + 1)

        # Si el hijo quedó vacío tras borrar, cortar la referencia
        if eliminado and podar_hijo:
            self.__nodos[nodo_idx].hijos[idx_letra] = None

        # ¿Este nodo debe podarse?
        debe_podarse = (not self.__nodos[nodo_idx].es_fin) and all(
            h is None for h in self.__nodos[nodo_idx].hijos
        )
        return eliminado, debe_podarse

    # ---------Limpiar---------
    def limpie(self) -> None:
        """Limpia el Trie completamente."""
        self.__nodos = [NodoTrieArray()]
        self.__tamaño = 0

    # ---------Imprimir---------
    def imprima(self) -> None:
        """Imprime todas las palabras del Trie en orden alfabético."""
        palabras: List[str] = []
        self.__recorrer(0, "", palabras)
        if palabras:
            print(" -> ".join(palabras))
        else:
            print("(Trie vacío)")

    def __recorrer(self, nodo_idx: int, prefijo: str, palabras: List[str]) -> None:
        nodo = self.__nodos[nodo_idx]
        if nodo.es_fin:
            palabras.append(prefijo)
        for i, hijo in enumerate(nodo.hijos):
            if hijo is not None:
                self.__recorrer(hijo, prefijo + chr(ord("a") + i), palabras)

    # ---------Done---------
    def done(self) -> None:
        """Libera la estructura."""
        self.__nodos = []
        self.__tamaño = 0

    # ---------Representación---------
    def __str__(self) -> str:
        palabras: List[str] = []
        if self.__nodos:  # evitar acceder a índice 0 si está liberado
            self.__recorrer(0, "", palabras)
        return "[" + ", ".join(palabras) + "]"
