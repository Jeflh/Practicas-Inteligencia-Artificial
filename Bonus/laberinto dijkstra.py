import random
import os
import sys
import time

def generar_terreno():
    # Definimos la matriz de 10x10 que representa el plano
    matriz = [['🔲' for i in range(10)] for j in range(10)]

    # Agregamos obstáculos aleatorios al plano
    for i in range(30):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        matriz[x][y] = '🌑'

    # Definimos las coordenadas del punto origen y destino
    origen = (random.randint(0, 9), random.randint(0, 9))
    matriz[origen[0]][origen[1]] = '🔴'
    destino = (random.randint(0, 9), random.randint(0, 9))
    matriz[destino[0]][destino[1]] = '⭐'

    return matriz, origen, destino

# Función para obtener los vecinos de un nodo dado
def obtener_vecinos(nodo):
    x, y = nodo
    vecinos = []
    if x > 0 and matriz[x-1][y] != '🌑':   # nodo de arriba
        vecinos.append((x-1, y))
    if x < 9 and matriz[x+1][y] != '🌑':  # nodo de abajo
        vecinos.append((x+1, y))
    if y > 0 and matriz[x][y-1] != '🌑':  # nodo de la izquierda
        vecinos.append((x, y-1))
    if y < 9 and matriz[x][y+1] != '🌑':  # nodo de la derecha
        vecinos.append((x, y+1))
    return vecinos

# Función para realizar la búsqueda utilizando el algoritmo de Dijkstra
def busqueda_dijkstra(origen, destino):
    distancia = {nodo: sys.maxsize for nodo in [(x, y) for x in range(10) for y in range(10)]}
    distancia[origen] = 0
    visitados = set()
    camino = {nodo: [] for nodo in [(x, y) for x in range(10) for y in range(10)]}
    while True:
        nodo_actual = None
        min_distancia = sys.maxsize
        for nodo in [(x, y) for x in range(10) for y in range(10)]:
            if nodo in visitados:
                continue
            if distancia[nodo] < min_distancia:
                nodo_actual = nodo
                min_distancia = distancia[nodo]
        if nodo_actual is None:
            break
        visitados.add(nodo_actual)
        if nodo_actual == destino:
            break
        for vecino in obtener_vecinos(nodo_actual):
            distancia_vecino = distancia[nodo_actual] + 1
            if distancia_vecino < distancia[vecino]:
                distancia[vecino] = distancia_vecino
                camino[vecino] = camino[nodo_actual] + [nodo_actual]
    return camino[destino] if camino[destino] else None


if __name__ == '__main__':
    opcion = 4

    while True:
        os.system('cls')
        # Generamos el terreno
        if opcion != -1:
            matriz, origen, destino = generar_terreno()

        # Imprimimos la representación del terreno en ASCII
        print("Terreno generado:\n")
        for fila in matriz:
            print(' '.join(str(x) for x in fila))

        print("\n\tMenu")
        print("1. Búsqueda Dijkstra")
        print("4. Generar otro terreno")
        print("0. Salir")

        try:
            opcion = int(input("> "))
        except ValueError:
            opcion = -1

        if opcion == 1:
            tiempo_inicial = time.time()
            # Llamamos a la función de búsqueda en amplitud e imprimimos el resultado
            resultado = busqueda_dijkstra(origen, destino)
            tiempo_final = time.time()
            tiempo_ejecucion = (tiempo_final - tiempo_inicial)
            if resultado is not None:
                print("\nEl camino más corto desde el origen hasta el destino es:\n")
                for nodo in resultado:
                    matriz[nodo[0]][nodo[1]] = '🚀'
                
                # Emojis de origen y destino
                matriz[origen[0]][origen[1]] = '🔴'
                matriz[destino[0]][destino[1]] = '⭐'

                for fila in matriz:
                    print(' '.join(str(x) for x in fila))
                print("\nTiempo de ejecución: " + str(tiempo_ejecucion) + " segundos")
            else:
                print("\nNo hay camino posible desde el origen hasta el destino")
            
            os.system('pause')

        elif opcion == 4:
            continue

        elif opcion == 0:
            break

        else:
            opcion = -1
            print("\nOpción no válida, intente de nuevo.")
            os.system('pause')
