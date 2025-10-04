from tarea1.diccionario import Diccionario
import time

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

    def __str__(self) -> str:
        return str(self.__tabla)
