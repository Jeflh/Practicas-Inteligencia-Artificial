import random, os
from queue import Queue

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

# Función para realizar la búsqueda en amplitud
def busqueda_en_amplitud(origen, destino):
    visitados = set()
    cola = Queue()
    cola.put((origen, 0, []))
    while not cola.empty():
        nodo, distancia, camino = cola.get()
        if nodo == destino:
            return camino + [nodo]
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in obtener_vecinos(nodo):
                cola.put((vecino, distancia+1, camino+[nodo]))
    return None

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
        print("1. Búsqueda en amplitud")
        print("4. Generar otro terreno")
        print("0. Salir")

        try:
            opcion = int(input("> "))
        except ValueError:
            opcion = -1

        if opcion == 1:
            # Llamamos a la función de búsqueda en amplitud e imprimimos el resultado
            resultado = busqueda_en_amplitud(origen, destino)

            if resultado is not None:
                print("\nEl camino más corto desde el origen hasta el destino es:\n")
                
                # Imprimimos el camino encontrado
                for nodo in resultado:
                    matriz[nodo[0]][nodo[1]] = '🚀'
                
                    # Emojis de origen y destino
                    matriz[origen[0]][origen[1]] = '🔴'
                    matriz[destino[0]][destino[1]] = '🚩'

                for fila in matriz:
                    print(' '.join(str(x) for x in fila))
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

        
   