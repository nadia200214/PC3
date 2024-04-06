import random

def generar_numeros_aleatorios():
    """
    Genera 20 números enteros aleatorios entre 0 y 100.
    
    Returns:
        list: Lista de 20 números enteros aleatorios.
    """
    numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
    return numeros_aleatorios

def mostrar_lista(lista):
    """
    Muestra una lista por pantalla.
    
    Args:
        lista (list): La lista a mostrar.
    """
    print("Lista de números:")
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_lista(lista):
    """
    Ordena los valores de una lista y la muestra por pantalla.
    
    Args:
        lista (list): La lista a ordenar y mostrar.
    """
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for numero in lista_ordenada:
        print(numero, end=" ")
    print()