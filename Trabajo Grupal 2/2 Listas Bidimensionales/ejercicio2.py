# Definimos la cantidad de columnas con las que se va a trabajar.
columnas = int(input("Ingrese la cantidad de columnas. "))
# Definimos la cantidad de filas con las que se va a trabajar.
filas = int(input("Ingrese la cantidad de filas. "))

matriz = []
valor = 1 # Indica en qué número empiezan los valores de la matriz.
# Armamos la matriz (por ahora vacía) usando bucles anidados.
for i in range(columnas):
    fil = [] # Creamos una variable que acumule las filas.
    for o in range(filas):
        fil.append(valor) # Le asiganos un valor incrementativo.
        valor += 1
    matriz.append(fil) # Pegamos cada fila creada en la matriz.
print(f"La matriz es: {matriz}.")

# Finalmente recorremos la matriz, añadiendo el total de cada fila a "total".
total = 0
for i in range(columnas):
    total += sum(matriz[i])
print()
print(f"El total de la variable es {total}.")
