# Codigo del metodo burbuja
def metodo_burbuja(lista):
    n = len(lista)
    for i in range(1, n):
        for j in range(0, n - 1):
            if lista[j] < lista[j + 1]:
                cambio = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = cambio
    return lista
