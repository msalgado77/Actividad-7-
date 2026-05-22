# Importamos random para que de uno al 20 sea de manera desordenada
import random
# Inportamos estos para hacer facilmente el determinante
import numpy as np

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
# Agregamos que numeros randoms saldran
        fila.append(random.randint(1, 20))
    matriz.append(fila)


print("Matriz que generamos para ti es:")
for fila in matriz:
    print(fila)

# Se puede hacer la operración de determinante solo si las filas son las mismas que las columnas
if filas == columnas:
# Se utiliza la operacion ya que con diferentes matrices son diferentes procesos 
    determinante = int(round(np.linalg.det(np.array(matriz))))
    print("Determinante:", determinante)
else:
    print("No se puede calcular el determinante: la matriz no es cuadrada.")
