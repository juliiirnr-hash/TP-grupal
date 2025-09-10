# Definimos una función que cree una matriz (llamada "matriz") por nosotros.
def creaLista(columnas, filas):
    matriz = []
    valor = 0
    # Armamos la lista (por ahora vacía) usando bucles anidados.
    for i in range(columnas):
        columnas = [] # Creamos un placeholder para las columnas.
        for o in range(filas):
            columnas.append(valor) # Le asiganos un valor incrementativo.
            valor += 1
        matriz.append(columnas) # Pegamos cada fila creada en la lista.
    print(matriz)
    return matriz

# Llamamos a la función.
matriz = creaLista(int(input("Ingrese la cantidad de columnas. ")), int(input("Ingrese la cantidad de filas. ")))
