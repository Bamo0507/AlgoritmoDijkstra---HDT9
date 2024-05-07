#Importar las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt
import heapq

#MÉTODO PARA HACER EL RECORRIDO CON EL ALGORITMO DE DIJKSTRA
def dijkstra(Grafo, inicio):
    # Inicializar las distancias de todos los nodos como infinito
    distancias = {nodo: float('inf') for nodo in rutas}
    # Inicializar el diccionario de rutas
    rutas_completas = {nodo: [] for nodo in rutas}
    # La distancia al nodo de inicio es 0
    distancias[inicio] = 0
    # Inicializar la cola de prioridad
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        # Sacar el nodo con la distancia mínima de la cola
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Recorrer los nodos vecinos del nodo actual
        for vecino, costo in rutas[nodo_actual].items():
            # Calcular la nueva distancia sumando el costo actual al costo acumulado
            distancia_nueva = distancia_actual + costo
            # Si la nueva distancia es menor que la distancia almacenada previamente
            if distancia_nueva < distancias[vecino]:
                # Actualizar la distancia
                distancias[vecino] = distancia_nueva
                # Actualizar la ruta completa
                rutas_completas[vecino] = rutas_completas[nodo_actual] + [nodo_actual]
                # Agregar el nodo a la cola de prioridad con su nueva distancia
                heapq.heappush(cola_prioridad, (distancia_nueva, vecino))

    return distancias, rutas_completas
  
#MÉTODO PRESENTAR INFORMACIÓN
def establecerRutas(rutas, salida):
    distancias, rutas_completas = dijkstra(rutas, salida)
    resultados = {}
    for destino, distancia in distancias.items():
        if distancia == float('inf'):
            resultados[destino] = ("NO SE PUEDE LLEGAR", [])
        else:
            resultados[destino] = (distancia, rutas_completas[destino] + [destino])
    return resultados

# Primero se hará la lectura del archivo
rutas = {}
with open('rutas.txt', 'r') as file:
    for line in file:
        # Limpiar las comillas dobles de la línea
        line = line.replace('"', '')
        salida, destino, costo = line.strip().split(', ')
        costo = int(costo)
        # Agregar rutas con costo
        # Se toma en cuenta para ir de X a Y, y de Y a X
        rutas.setdefault(salida, {})[destino] = costo
        rutas.setdefault(destino, {})[salida] = costo

# Impresión de diccionarios
print("Las rutas establecidas son: ")
print(rutas)

#Generar grafos en base a las rutas
Grafo = nx.Graph()

for estacion in rutas.keys():
    Grafo.add_node(estacion)
for salida, destinos in rutas.items():
    for destino, costo in destinos.items():
        Grafo.add_edge(salida, destino, weight=costo)
        
#VER GRAFO DE MANERA VISUAL        
# Posiciones de los nodos
pos = nx.spring_layout(Grafo)

# Dibujar nodos
nx.draw(Grafo, pos, with_labels=True, node_color='pink', node_size=150)

# Dibujar bordes con pesos
labels = nx.get_edge_attributes(Grafo, 'weight')
nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=labels, font_size=8)

# Mostrar el gráfico
plt.show()

#SOLICITUD DE ESTACIÓN DE SALIDA
systemON = True
while(systemON):
    print("\nLas estacioens disponibles son:")
    print("""
    1. Pueblo Paleta
    2. Aldea Azalea
    3. Ciudad Safiro
    4. Ciudad Lavanda
    5. Aldea Fuego
    COLOCA 6 PARA SALIR
        """)
    opcion = input("Por favor, ingrese su opción: ")
    if opcion == "6":
        print("Que tenga un buen día.")
        systemON = False
    elif opcion == "1":
        salida = "Pueblo Paleta"
        resultados = establecerRutas(rutas, salida)
        print("Distancias y rutas desde PUEBLO PALETA a toos los destinos: ")
        for destino, (distancia, ruta) in resultados.items():
            print(destino, "-", "tiene un costo de", distancia, ", Se debe pasar por las estaciones:", ruta)
            
    elif opcion == "2":
        salida = "Aldea Azalea"
        resultados = establecerRutas(rutas, salida)
        print("Distancias y rutas desde ALDEA AZALEA a toos los destinos: ")
        for destino, (distancia, ruta) in resultados.items():
            print(destino, "-", "tiene un costo de", distancia, ", Se debe pasar por las estaciones:", ruta)
            
    elif opcion=="3":
        salida="Ciudad Safiro"
        resultados = establecerRutas(rutas, salida)
        print("Distancias y rutas desde CIUDAD SAFIRO a toos los destinos: ")
        for destino, (distancia, ruta) in resultados.items():
            print(destino, "-", "tiene un costo de", distancia, ", Se debe pasar por las estaciones:", ruta)
            
    elif opcion=="4":
        salida="Ciudad Lavanda"
        resultados = establecerRutas(rutas, salida)
        print("Distancias y rutas desde CIUDAD LAVANDA a toos los destinos: ")
        for destino, (distancia, ruta) in resultados.items():
            print(destino, "-", "tiene un costo de", distancia, ", Se debe pasar por las estaciones:", ruta)
            
    elif opcion=="5":
        salida="Aldea Fuego"
        resultados = establecerRutas(rutas, salida)
        print("Distancias y rutas desde ALDEA FUEGO a toos los destinos: ")
        for destino, (distancia, ruta) in resultados.items():
            print(destino, "-", "tiene un costo de", distancia, ", Se debe pasar por las estaciones:", ruta)
        
    else:
        print("Por favor, seleccione una opción válida.")
        
