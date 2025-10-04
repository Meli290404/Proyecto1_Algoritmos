from tarea1.listaordenadadinamica import ListaOrdenadaDinamica
from tarea1.listaordenadaestatica import ListaOrdenadaEstatica
from tarea1.tablahashabierta import TablaHashAbierta

def seleccionar_diccionario():
    print("\nSeleccione la implementación:")
    print("1. Lista Ordenada Dinámica (punteros)")
    print("2. Lista Ordenada Estática (arreglo)")
    print("3. Tabla Hash Abierta")
    opcion = input("Opción: ")
    if opcion == "1":
        return ListaOrdenadaDinamica()
    elif opcion == "2":
        return ListaOrdenadaEstatica()
    elif opcion == "3":
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
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    dicc = seleccionar_diccionario()
    menu(dicc)
