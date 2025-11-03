# -*- coding: utf-8 -*-
"""
Programa de análisis de rendimiento y uso de espacio
para las estructuras del Modelo Diccionario.
Tercera etapa del proyecto de Algoritmos y Estructuras de Datos.
"""

import time
import sys
import random
import string

from tarea1.listaordenadadinamica import ListaOrdenadaDinamica
from tarea1.listaordenadaestatica import ListaOrdenadaEstatica
from tarea1.tablahashabierta import TablaHashAbierta
from tarea1.abbpunteros import ABBPunteros
from tarea1.abbvectorheap import ABBVectorHeap
from tarea1.triepunteros import TriePunteros
from tarea1.triearreglos import TrieArreglos


def generar_palabras(n: int, longitud: int = 20) -> list[str]:
    """
    Genera n palabras aleatorias de longitud fija.
    Cada palabra contiene solo letras 'a'..'z'.
    """
    return [''.join(random.choices(string.ascii_lowercase, k=longitud)) for _ in range(n)]


def medir_tiempos(diccionario, datos: list[str]):
    """
    Mide los tiempos de inserción, búsqueda y eliminación
    sobre un diccionario dado.
    Retorna: (tiempo_insert, tiempo_busqueda, tiempo_borrado, memoria_en_bytes)
    """
    # Inserción 
    inicio = time.perf_counter()
    for palabra in datos:
        diccionario.inserte(palabra)
    tiempo_insert = time.perf_counter() - inicio

    # Búsqueda 
    inicio = time.perf_counter()
    for palabra in datos:
        diccionario.miembro(palabra)
    tiempo_busqueda = time.perf_counter() - inicio

    # Borrado
    inicio = time.perf_counter()
    for palabra in datos:
        diccionario.borre(palabra)
    tiempo_borrado = time.perf_counter() - inicio

    # --- Medición de memoria ---
    memoria = sys.getsizeof(diccionario)

    return tiempo_insert, tiempo_busqueda, tiempo_borrado, memoria

def ejecutar_analisis():
    print("\n>>> Iniciando pruebas de rendimiento")
    
    tamanos = [1000, 5000, 10000]  # Ajusta según necesites
    for n in tamanos:
        datos = generar_palabras(n)
        estructuras = [
            ListaOrdenadaDinamica(),
            ListaOrdenadaEstatica(20000),
            TablaHashAbierta(),
            ABBPunteros(),
            ABBVectorHeap(),
            TriePunteros(),
            TrieArreglos()
        ]
        for estructura in estructuras:
            tiempos = medir_tiempos(estructura, datos)
            print(f"{estructura.__class__.__name__} (n={n}):")
            print(f"Inserción: {tiempos[0]:.4f}s")
            print(f"Búsqueda: {tiempos[1]:.4f}s")
            print(f"Borrado: {tiempos[2]:.4f}s")
            print(f"Memoria: {tiempos[3]} bytes\n")

input("\nPresione Enter para continuar...")


