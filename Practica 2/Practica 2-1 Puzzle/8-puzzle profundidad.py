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

# Función para buscar la solución por amplitud
def busqueda_amplitud(estado_inicial):
    cola = deque([(estado_inicial, [])])
    explorado = set()
    while cola: 
        estado_actual, camino = cola.popleft() # Extraer el primer estado de la cola
        explorado.add(str(estado_actual))
        for sucesor in sucesores(estado_actual): 
            if str(sucesor) not in explorado: # Si el sucesor no ha sido explorado
                if es_objetivo(sucesor): # Si es el estado objetivo, devolver el camino
                    return camino + [sucesor]  
                cola.append((sucesor, camino + [sucesor])) # Añadir el sucesor a la cola
    return None # No se ha encontrado solución

# Función para buscar la solución por profundidad
def busqueda_profundidad(estado_inicial):
    # Inicializar la pila de estados a visitar
    pila = [(estado_inicial, [])]
    # Inicializar el conjunto de estados visitados
    visitados = set()
    visitados.add(tuple(map(tuple, estado_inicial)))
    # Buscar el estado objetivo
    while len(pila) > 0:
        estado, camino = pila.pop()
        if es_objetivo(estado):
            # Construir el camino desde el estado inicial hasta el estado objetivo
            return camino + [estado]
        for sucesor in sucesores(estado):
            if tuple(map(tuple, sucesor)) not in visitados:
                pila.append((sucesor, camino + [estado]))
                visitados.add(tuple(map(tuple, sucesor)))
    return None

# Función para buscar la solución por profundidad limitada
def busqueda_profundidad_limitada(estado, limite):
    frontera = [(estado, [])]
    explorado = set() 
    while frontera:
        estado_actual, camino = frontera.pop() # Extraer el último estado de la frontera
        explorado.add(str(estado_actual)) 
        if es_objetivo(estado_actual): # Si es el estado objetivo, devolver el camino
            return camino + [estado_actual] 
        if len(camino) < limite: 
            for sucesor in sucesores(estado_actual): # Generar los sucesores del estado actual
                if str(sucesor) not in explorado: # Si el sucesor no ha sido explorado
                    frontera.append((sucesor, camino + [sucesor])) # Agregarlo a la frontera
    return 'corte' # Devolver corte si no se encontró la solución

# Función para buscar la solución por profundidad iterativa
def busqueda_profundidad_iterativa(estado):
    limite = 0 
    while True:
        solucion = busqueda_profundidad_limitada(estado, limite) # Buscar la solución
        if solucion != 'corte': # Si no se cortó la búsqueda
            return solucion
        limite += 1 # Incrementar el límite


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
        print("1. Búsqueda en amplitud")
        print("2. Búsqueda en profundidad")
        print("3. Búsqueda en profundidad iterativa")
        print("4. Generar otro estado")
        print("0. Salir")
        try:
            opcion = int(input("> "))
        except ValueError:
            opcion = -1

        if opcion == 1: 
            tiempo_inicial = time.time()

            # Buscar la solución por amplitud
            solucion = busqueda_amplitud(estado_inicial)

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

        elif opcion == 2:
            tiempo_inicial = time.time()

            # Buscar la solución por profundidad
            solucion = busqueda_profundidad(estado_inicial)

            tiempo_final = time.time()
            tiempo_ejecucion = int(tiempo_final - tiempo_inicial)
            minutos, segundos = divmod(tiempo_ejecucion, 60)
        
            # Imprimir la solución
            print('\nSolución en profundidad: \n')
            for estado in solucion:
                for fila in estado:
                    print(fila)
                print()
            print(f'Tiempo de ejecución: {minutos:01d}:{segundos:02d}')
            os.system('pause')

        elif opcion == 3:
            tiempo_inicial = time.time()

            # Buscar la solución por profundidad iterativa
            solucion = busqueda_profundidad_iterativa(estado_inicial)

            tiempo_final = time.time()
            tiempo_ejecucion = (tiempo_final - tiempo_inicial)

            # Imprimir la solución
            print('\nSolución en profundidad iterativa: \n')
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
