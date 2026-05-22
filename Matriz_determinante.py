import random

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        # Genera un entero aleatorio entre 1 y 20
        fila.append(random.randint(1, 20))
    matriz.append(fila)


print("Matriz que generamos para ti es:")
for fila in matriz:
    print(fila)
    