from tarea1.listaordenadadinamica import ListaOrdenadaDinamica
from tarea1.listaordenadaestatica import ListaOrdenadaEstatica
from tarea1.tablahashabierta import TablaHashAbierta

def seleccionar_diccionario():
    print("\nSeleccione la implementación:")
    print("1. Lista Ordenada Dinámica (punteros)")
    print("2. Lista Ordenada Estática (arreglo)")
    print("3. Tabla Hash Abierta")
    opcion = input("Opción: ")
    print(f"[DEBUG] Opción leída: {opcion}")
    if opcion == "1":
        print("[DEBUG] Creando ListaOrdenadaDinamica")
        return ListaOrdenadaDinamica()
    elif opcion == "2":
        print("[DEBUG] Creando ListaOrdenadaEstatica")
        return ListaOrdenadaEstatica()
    elif opcion == "3":
        print("[DEBUG] Creando TablaHashAbierta")
        return TablaHashAbierta()
    else:
        print("Opción inválida, usando ListaOrdenadaDinamica por defecto.")
        return ListaOrdenadaDinamica()

def menu(diccionario):
    while True:
        print("\nMenú de operaciones")
        print("1. Insertar")
        print("2. Eliminar")
        print("3. Buscar")
        print("4. Imprimir")
        print("5. Limpiar")
        print("6. Salir")
        # Opciónes extra para tabla hash
        if isinstance(diccionario, TablaHashAbierta):
            print("7. Evaluar uniformidad de hash (prueba sintética)")
            print("8. Forzar rehash y medir tiempo")
        
        opcion = input("Opción: ")

        if opcion == "1":
            e = input("Elemento: ")
            diccionario.inserte(e)
        elif opcion == "2":
            e = input("Elemento: ")
            diccionario.borre(e)
        elif opcion == "3":
            e = input("Elemento: ")
            print("Miembro:", diccionario.miembro(e))
        elif opcion == "4":
            diccionario.imprima()
        elif opcion == "5":
            diccionario.limpie()
        elif opcion == "6":
            break
        elif opcion == "7" and isinstance(diccionario, TablaHashAbierta):
            try:
                n = int(input("¿Cuántas claves aleatorias generar? [ej. 5000]: "))
            except ValueError:
                n = 1000
            diccionario.evaluar_uniformidad(n=n, imprimir=True)
        elif opcion == "8" and isinstance(diccionario, TablaHashAbierta):
            t = diccionario.forzar_rehash_y_medir()
            print(f"Rehash forzado tomó {t:.6f} s")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    dicc = seleccionar_diccionario()
    menu(dicc)
