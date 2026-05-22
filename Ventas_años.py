# Inportamos estos para hacer facilmente unos procesos
import numpy as np

vendedores = int(input("Ingrese el número de empleados que analizaremos: "))
años = int(input("Ingrese los años de operación de cada empleado: "))

# Se forma una matriz de zeros
ventas = np.zeros((vendedores, años))

for i in range(vendedores):
    print(f"Vendedor {i+1} ")
    for j in range(años):
        ventas[i, j] = float(input("Ingrese las ventas del año:"))

# Sumar Filas con el axis
total_vendedores = ventas.sum(axis=1)
total_años = ventas.sum(axis=0)
gran_total = ventas.sum()

print("Total por vendedor:", total_vendedores)
print("Total por año:", total_años)
print("Gran total de la empresa:", gran_total)
