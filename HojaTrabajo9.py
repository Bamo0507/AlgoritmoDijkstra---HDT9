#Importar las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt


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
