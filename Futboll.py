num_equipos = int(input("¿Cuántos equipos hay?: "))
tabla = {}

for i in range(num_equipos):
    nombre = input("Nombre del equipo: ")
# Variables de los datos que se piden
    tabla[nombre] = {"PJ": 0, "PG": 0, "PE": 0, "PP": 0, "GF": 0, "GC": 0, "PTS": 0}


num_partidos = int(input("¿Cuántos partidos han jugado?: "))

# Lo que se ve se muestra al usuario y entra los datos
for i in range(num_partidos):
    print(f"Partido {i+1}:")
    local = input("Equipo Local: ").strip()
    gl = int(input(f"Goles de {local}: "))
    visitante = input("Equipo Visitante: ").strip()
    gv = int(input(f"Goles de {visitante}: "))

# Actualizaciones
    tabla[local]["PJ"] += 1
    tabla[local]["GF"] += gl
    tabla[local]["GC"] += gv
    tabla[visitante]["PJ"] += 1
    tabla[visitante]["GF"] += gv
    tabla[visitante]["GC"] += gl

# Poner los puntos por como les va en el partido
    if gl > gv:
        tabla[local]["PG"] += 1
        tabla[local]["PTS"] += 3
        tabla[visitante]["PP"] += 1
    elif gv > gl:
        tabla[visitante]["PG"] += 1
        tabla[visitante]["PTS"] += 3
        tabla[local]["PP"] += 1
    else:
        tabla[local]["PE"] += 1
        tabla[visitante]["PE"] += 1
        tabla[local]["PTS"] += 1
        tabla[visitante]["PTS"] += 1


print("TABLA DE POSICIONES")
# Se deja reservado unos espacios para que se vea organizado cuando salga
print(f"{'EQUIPO':<15} | {'PJ':<3} | {'GF':<3} | {'GC':<3} | {'PTS':<3}")

# Clasificación mas ordenada
ordenados = sorted(tabla.items(), key=lambda x: x[1]["PTS"], reverse=True)

for nombre, datos in ordenados:
    print(
        f"{nombre:<15},"
        f"{datos['PJ']:<3},"
        f"{datos['GF']:<3},"
        f"{datos['GC']:<3},"
        f"{datos['PTS']:<3}"
    )
