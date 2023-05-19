import random, os, time
from collections import deque

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
                # Devolver los sucesores
                return sucesores

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


# Función para calcular la distancia Manhattan entre dos puntos en una matriz 3x3
def distancia_manhattan(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return abs(x1 - x2) + abs(y1 - y2)


# Función para buscar la posición de un elemento en el estado
def buscar_posicion(estado, elemento):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == elemento:
                return (i, j)


# Función para buscar la solución por el algoritmo "Primero el mejor"
def busqueda_primero_el_mejor(estado_inicial):
    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    cola_prioridad = []
    explorado = set()
    
    # Calcular la heurística para el estado inicial
    heuristica_inicial = distancia_manhattan(buscar_posicion(estado_inicial, 0), (2, 2))
    cola_prioridad.append((heuristica_inicial, estado_inicial, []))
    
    while cola_prioridad:
        _, estado_actual, camino = cola_prioridad.pop(0)  # Extraer el estado con menor heurística
        explorado.add(str(estado_actual))
        
        if estado_actual == objetivo:
            return camino + [estado_actual]
        
        for sucesor in sucesores(estado_actual):
            if str(sucesor) not in explorado:
                heuristica_sucesor = distancia_manhattan(buscar_posicion(sucesor, 0), (2, 2))
                cola_prioridad.append((heuristica_sucesor, sucesor, camino + [sucesor]))
        
        # Ordenar la cola de prioridad según la heurística
        cola_prioridad.sort(key=lambda x: x[0])
    
    return None



# Función para buscar la solución por amplitud
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
        print("1. Búsqueda primero el mejor")
        print("4. Generar otro estado")
        print("0. Salir")
        try:
            opcion = int(input("> "))
        except ValueError:
            opcion = -1

        if opcion == 1: 
            tiempo_inicial = time.time()

            # Buscar la solución por amplitud
            solucion = busqueda_primero_el_mejor(estado_inicial)

            tiempo_final = time.time()
            tiempo_ejecucion = (tiempo_final - tiempo_inicial)

            # Imprimir la solución
            print('\nSolución en amplitud: \n')
            for estado in solucion:
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
            opcion = -1
            print("\nOpción no válida, intente de nuevo.")
            os.system('pause')