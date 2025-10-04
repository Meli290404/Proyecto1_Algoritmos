from tarea1.diccionario import Diccionario
import time
import random
import string
from collections import Counter
import math

class TablaHashAbierta(Diccionario):
    def __init__(self, capacidad_inicial=10):
        self.__capacidad = capacidad_inicial
        self.__tabla = [[] for _ in range(self.__capacidad)]
        self.__tamaño = 0

    def __hash_func(self, clave: str) -> int:
        """Función hash simple (puedes mejorarla si quieres)."""
        return sum(ord(c) for c in clave) % self.__capacidad

    def inserte(self, elemento: str):
        indice = self.__hash_func(elemento)
        bucket = self.__tabla[indice]
        bucket.append(elemento)
        self.__tamaño += 1
        if self.__tamaño / self.__capacidad > 0.7:  # factor de carga
            self.__rehash()

    def borre(self, elemento: str):
        indice = self.__hash_func(elemento)
        bucket = self.__tabla[indice]
        if elemento in bucket:
            bucket.remove(elemento)
            self.__tamaño -= 1

    def limpie(self):
        self.__tabla = [[] for _ in range(self.__capacidad)]
        self.__tamaño = 0

    def miembro(self, elemento: str) -> bool:
        indice = self.__hash_func(elemento)
        return elemento in self.__tabla[indice]

    def imprima(self):
        for i, bucket in enumerate(self.__tabla):
            print(f"{i}: {bucket}")

    def done(self):
        self.__tabla = []
        self.__capacidad = 0
        self.__tamaño = 0

    def __rehash(self):
        start = time.perf_counter()
        vieja_tabla = self.__tabla
        self.__capacidad *= 2
        self.__tabla = [[] for _ in range(self.__capacidad)]
        self.__tamaño = 0
        for bucket in vieja_tabla:
            for elemento in bucket:
                self.inserte(elemento)
        end = time.perf_counter()
        print(f"Rehash completado en {end - start:.6f} segundos.")

    def forzar_rehash_y_medir(self) -> float:
        """Fuerza un rehash manualmente y retorna el tiempo que tomó."""
        import time
        inicio = time.perf_counter()
        self.__rehash()
        fin = time.perf_counter()
        return fin - inicio
    
    def evaluar_hash(self):
        distribucion = [len(bucket) for bucket in self.__tabla]
        print("Distribución de elementos por bucket:", distribucion)
    
    def evaluar_uniformidad(self, n: int = 1000, imprimir: bool = True):
        """
        Genera n claves aleatorias (strings de 20 letras 'a'..'z'), las pasa por la
        función hash y mide qué tan uniformemente se distribuyen en los buckets.

        Retorna un diccionario con métricas básicas (ocupación por bucket, promedio,
        mínimo, máximo y desviación estándar). Si imprimir=True, también muestra
        un resumen por consola.
        """
        # 1) Generar n claves aleatorias con el mismo dominio que pide el enunciado (20 letras a..z)
        claves = [
            ''.join(random.choices(string.ascii_lowercase, k=20))
            for _ in range(n)
        ]

        # 2) Calcular el índice (bucket) asignado por la función hash para cada clave
        #    OJO: estamos dentro de la clase, así que podemos llamar a self.__hash_func(...) directamente
        indices = [self.__hash_func(c) for c in claves]

        # 3) Contar cuántas claves cayeron en cada bucket
        conteo_por_indice = Counter(indices)

        # 4) Convertir ese conteo a una lista de longitud = capacidad (para ver también los buckets vacíos)
        ocupacion = [0] * self.__capacidad
        for idx, cnt in conteo_por_indice.items():
            ocupacion[idx] = cnt

        # 5) Calcular métricas de uniformidad
        promedio = n / self.__capacidad                     # esperado por bucket si fuera perfectamente uniforme
        minimo = min(ocupacion)
        maximo = max(ocupacion)
        varianza = sum((x - promedio) ** 2 for x in ocupacion) / self.__capacidad
        desv_estandar = math.sqrt(varianza)

        if imprimir:
            print(f"\n== Evaluación de uniformidad de hash ==")
            print(f"Capacidad actual de la tabla: {self.__capacidad}")
            print(f"Número de claves generadas: {n}")
            print(f"Factor de carga simulado: {n/self.__capacidad:.2f}")
            print(f"Ocupación por bucket (primeros 50 shown si muy larga):")
            # Evitar imprimir miles de números si la capacidad es grande
            vista = ocupacion[:50]
            print(vista if len(ocupacion) > 50 else ocupacion)
            print(f"Promedio esperado por bucket: {promedio:.2f}")
            print(f"Mínimo: {minimo}, Máximo: {maximo}, Desv. estándar: {desv_estandar:.2f}\n")

        # 6) Devolver los datos por si quieres graficar o analizarlos aparte
        return {
            "ocupacion_buckets": ocupacion,
            "promedio": promedio,
            "minimo": minimo,
            "maximo": maximo,
            "desviacion_estandar": desv_estandar
        }

    def __str__(self) -> str:
        return str(self.__tabla)
