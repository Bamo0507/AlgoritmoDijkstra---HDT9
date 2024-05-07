# Algoritmo de Dijkstra para Búsqueda de Rutas Más Cortas

Este código implementa el algoritmo de Dijkstra para encontrar la ruta más corta entre dos nodos en un grafo ponderado.

## Requisitos

- Python 3.x
- networkx
- matplotlib

## Descripción

El algoritmo de Dijkstra es un algoritmo de búsqueda de rutas más cortas que encuentra la ruta más corta entre un nodo de inicio y todos los demás nodos en un grafo con pesos no negativos. 

## Funcionalidades

- **dijkstra(Grafo, inicio)**: Implementa el algoritmo de Dijkstra para calcular la ruta más corta desde un nodo de inicio a todos los demás nodos en un grafo ponderado.
- **establecerRutas(rutas, salida)**: Utiliza el algoritmo de Dijkstra para encontrar las distancias y rutas más cortas desde un nodo de salida a todos los demás nodos en un grafo ponderado.

## Uso

1. Ejecuta el script.
2. Selecciona una estación de salida.
3. El programa mostrará los costos y rutas más cortas desde la estación de salida seleccionada a todas las demás estaciones.

## Archivo de Entrada (rutas.txt)

El programa espera un archivo de texto llamado "rutas.txt" en el mismo directorio que el script. Cada línea del archivo debe contener tres elementos separados por comas: el nodo de salida, el nodo de destino y el costo de viajar de la salida al destino.
