import random
import os
import time
# Función para comprobar si se ha llegado al estado objetivo
def es_objetivo(estado):
    return estado == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Función para generar los sucesores de un estado dado
def sucesores(estado):
    sucesores = []
    # Buscar el espacio en blanco
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                # Mover hacia arriba
                if i > 0:
                    sucesor = [fila[:] for fila in estado]
                    sucesor[i][j], sucesor[i-1][j] = sucesor[i-1][j], sucesor[i][j]
                    sucesores.append(sucesor)
                # Mover hacia abajo
                if i < 2:
                    sucesor = [fila[:] for fila in estado]
                    sucesor[i][j], sucesor[i+1][j] = sucesor[i+1][j], sucesor[i][j]
                    sucesores.append(sucesor)
                # Mover hacia la izquierda
                if j > 0:
                    sucesor = [fila[:] for fila in estado]
                    sucesor[i][j], sucesor[i][j-1] = sucesor[i][j-1], sucesor[i][j]
                    sucesores.append(sucesor)
                # Mover hacia la derecha
                if j < 2:
                    sucesor = [fila[:] for fila in estado]
                    sucesor[i][j], sucesor[i][j+1] = sucesor[i][j+1], sucesor[i][j]
                    sucesores.append(sucesor)
    return sucesores

# Función para calcular el costo de moverse desde el estado actual al siguiente estado
def costo_movimiento(estado_actual, siguiente_estado):
    return 1

# Función para buscar la solución por el algoritmo de Dijkstra
def busqueda_dijkstra(estado_inicial):
    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distancia = {}  # Distancia acumulada desde el estado inicial hasta el estado actual
    camino = {}  # Camino desde el estado inicial hasta el estado actual

    estado_inicial_str = str([[str(digito) for digito in fila] for fila in estado_inicial])
    objetivo_str = str([[str(digito) for digito in fila] for fila in objetivo])

    distancia[estado_inicial_str] = 0
    camino[estado_inicial_str] = []

    while estado_inicial_str != objetivo_str:
        sucesores_estado = sucesores(estado_inicial)

        for sucesor in sucesores_estado:
            sucesor_str = str([[str(digito) for digito in fila] for fila in sucesor])
            costo = costo_movimiento(estado_inicial, sucesor)

            if sucesor_str not in distancia or distancia[estado_inicial_str] + costo < distancia[sucesor_str]:
                distancia[sucesor_str] = distancia[estado_inicial_str] + costo
                camino[sucesor_str] = camino[estado_inicial_str] + [estado_inicial]

        del distancia[estado_inicial_str]

        min_distancia = float('inf')

        for estado, dist in distancia.items():
            if dist < min_distancia:
                min_distancia = dist
                estado_inicial_str = estado

    return camino[objetivo_str] + [objetivo]

# Función para generar un estado aleatorio válido
def estado_aleatorio():
    estado = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    movimientos = ['arriba', 'abajo', 'izquierda', 'derecha']
    n_movimientos = random.randint(20, 50)
    for i in range(n_movimientos):
        movimiento = random.choice(movimientos)
        espacio = 0
        for j in range(3):
            if espacio != 0:
                break
            for k in range(3):
                if estado[j][k] == 0:
                    espacio = (j, k)
                    break
        if movimiento == 'arriba':
            if espacio[0] > 0:
                estado[espacio[0]][espacio[1]] = estado[espacio[0]-1][espacio[1]]
                estado[espacio[0]-1][espacio[1]] = 0
        elif movimiento == 'abajo':
            if espacio[0] < 2:
                estado[espacio[0]][espacio[1]] = estado[espacio[0]+1][espacio[1]]
                estado[espacio[0]+1][espacio[1]] = 0
        elif movimiento == 'izquierda':
            if espacio[1] > 0:
                estado[espacio[0]][espacio[1]] = estado[espacio[0]][espacio[1]-1]
                estado[espacio[0]][espacio[1]-1] = 0
        elif movimiento == 'derecha':
            if espacio[1] < 2:
                estado[espacio[0]][espacio[1]] = estado[espacio[0]][espacio[1]+1]
                estado[espacio[0]][espacio[1]+1] = 0
    return estado

if __name__ == '__main__':
    opcion = 4

    while True:
        os.system('cls')

        # Generar un estado aleatorio
        if opcion != -1:
            estado_inicial = estado_aleatorio()

        # Imprimir el estado inicial
        print('Estado inicial: \n')
        for fila in estado_inicial:
            print('\t', fila)

        print("\n\tMenú")
        print("1. Búsqueda Dijkstra")
        print("4. Generar otro estado")
        print("0. Salir")
        try:
            opcion = int(input("> "))
        except ValueError:
            opcion = -1

        if opcion == 1:
            tiempo_inicial = time.time()
            # Buscar la solución por el algoritmo de Dijkstra
            camino = busqueda_dijkstra(estado_inicial)
            tiempo_final = time.time()
            tiempo_ejecucion = (tiempo_final - tiempo_inicial)

            # Imprimir la solución
            print('\nSolución por Dijkstra: \n')
            for estado in camino:
                for fila in estado:
                    print(fila)
                print()
            print(f'Tiempo de ejecución: {tiempo_ejecucion} segundos')
            os.system('pause')

        elif opcion == 4:
            continue

        elif opcion == 0:
            break

        else:
            os.system('pause')
