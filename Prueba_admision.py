print("CONFIGURACIÓN DEL EXAMEN")
correctas = input("Ingrese las 60 respuestas correctas: ")

n = int(input("¿Cuántos estudiantes harán el examen?: "))

# Todas las variables se nombran y empiezan vacias
estudiantes = []
suma_mat = suma_verb = suma_total = 0
mayor_puntaje = 0
credencial_mayor = ""

for i in range(n):
    print("Datos del estudiante")
    credencial = input("Número de credencial: ")
    respuestas = input("Ingrese las 60 respuestas: ")

# Se comparan las respuestas y se suman las que estan bien 
    puntaje_mat = sum(respuestas[j] == correctas[j] for j in range(30))
    puntaje_verb = sum(respuestas[j] == correctas[j] for j in range(30, 60))
    total = puntaje_mat + puntaje_verb

    suma_mat += puntaje_mat
    suma_verb += puntaje_verb
    suma_total += total

    if total > mayor_puntaje:
        mayor_puntaje, credencial_mayor = total, credencial

    estudiantes.append(
        {
            "credencial": credencial,
            "mat": puntaje_mat,
            "verb": puntaje_verb,
            "total": total,
        }
    )

    print(f"Matemáticas: {puntaje_mat} y Verbal: {puntaje_verb}")
    print(f" Total: {total}")

# Promedios
prom_mat = suma_mat / n
prom_verb = suma_verb / n
prom_total = suma_total / n

print(f"Promedio Matemáticas: {prom_mat}")
print(f"Promedio Verbal: {prom_verb}")
print(f"Promedio Total: {prom_total}")
print(f"Mayor puntaje: {mayor_puntaje} y Credencial {credencial_mayor}")

print("Estudiantes sobre o igual al promedio:")
for est in estudiantes:
    if est["total"] >= prom_total:
        print(f"Credencial {est['credencial']} con {est['total']} puntos")
