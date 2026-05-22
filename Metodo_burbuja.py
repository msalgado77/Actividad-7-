# Codigo del metodo burbuja
def metodo_burbuja(lista):
    n = len(lista)
# Creando una lista con los datos que se ingresan
    for i in range(1, n):
        for j in range(0, n - 1):
# Es un ciclo hasta que se complete la n ingresada (datos)
            if lista[j] < lista[j + 1]:
                cambio = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = cambio
    return lista


# Entrada de datos del usuario
print("Ingresa los números que quieras ordenar")
entrada = input("Acuerdate que es separado por espacios: ")

# Lista de datos enteros
numeros = list(map(int, entrada.split()))

print("Lista original:", numeros)
ordenada = metodo_burbuja(numeros)
print("Lista ordenada (mayor a menor):", ordenada)
