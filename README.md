
# 📘 Proyecto 1 - Modelo Diccionario (CI-0116 Análisis de Algoritmos y Estructuras de Datos)

## Estudiantes:
- Melissa Garita C23186
- Paula Sofia Grell C22977

---

## Descripción general

Este proyecto implementa el Modelo Diccionario, una estructura abstracta que permite almacenar y gestionar datos mediante diferentes estructuras de datos genéricas.  
Fue desarrollado en Python como parte de la Tarea Programada 1 del curso Análisis de Algoritmos y Estructuras de Datos.

Incluye implementaciones y comparaciones entre varias estructuras, con el fin de evaluar su eficiencia en tiempo y espacio, y un menú interactivo que facilita la prueba de las operaciones del diccionario.

---

## Estructuras implementadas (Etapa 1)

| Estructura | Descripción |
|-------------|-------------|
| **Lista Ordenada (genérica)** | Mantiene los elementos ordenados según un criterio de comparación. |
| **Lista Ordenada por punteros** | Usa nodos enlazados dinámicamente; permite inserciones y eliminaciones flexibles. |
| **Lista Ordenada por arreglos** | Usa un arreglo fijo; facilita el acceso rápido, pero requiere mover datos al insertar o borrar. |
| **Tabla Hash (genérica)** | Asocia claves con posiciones dentro de la tabla mediante una función hash. |
| **Tabla Hash abierta** | Maneja colisiones usando listas enlazadas (encadenamiento) y soporta rehashing dinámico. |

---

## Operaciones del Diccionario

Cada estructura implementa las siguientes operaciones:

| Operación | Descripción |
|------------|-------------|
| `inserte()` | Inserta un elemento en el diccionario. |
| `borre()` | Elimina un elemento existente. |
| `miembro()` | Verifica si un elemento está presente. |
| `limpie()` | Vacía la estructura. |
| `imprima()` | Muestra todos los elementos. |

---

## Evaluación del Hash y Redistribución

La clase `TablaHashAbierta` incluye métodos para analizar el comportamiento del hash:

- **`evaluar_uniformidad(n)`** → genera `n` claves aleatorias y mide su distribución entre los buckets.  
- **`forzar_rehash_y_medir()`** → duplica la capacidad de la tabla y mide el tiempo que tarda el proceso.

Estas funciones pueden ejecutarse desde el menú interactivo (opciones **7** y **8**).

---

## Ejecución del programa

Instala las dependencias y ejecuta:

```bash
uv sync
uv run tarea1

