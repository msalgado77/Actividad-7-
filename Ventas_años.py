import numpy as np

vendedores = int(input("Ingrese el número de empleados que analizaremos: "))
años = int(input("Ingrese los años de operación de cada empleado: "))

ventas = np.zeros((vendedores, años))

for i in range(vendedores):
    print(f"\n--- Vendedor {i+1} ---")
    for j in range(años):
        ventas[i, j] = float(input(f"Ingrese las ventas del año:"))

total_vendedores = ventas.sum(axis=1)
total_años = ventas.sum(axis=0)
gran_total = ventas.sum()

print("Total por vendedor:", total_vendedores)
print("Total por año:", total_años)
print("Gran total de la empresa:", gran_total)
