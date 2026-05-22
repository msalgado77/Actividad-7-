import random
import numpy as np

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.randint(1, 20))
    matriz.append(fila)

print("Matriz que generamos para ti es:")
for fila in matriz:
    print(fila)

if filas == columnas:
    determinante = int(round(np.linalg.det(np.array(matriz))))
    print("Determinante:", determinante)
else:
    print("No se puede calcular el determinante: la matriz no es cuadrada.")
