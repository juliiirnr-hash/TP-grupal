

# [ Ejercicio 4 ]:

columnas = int(input("Ingrese la cantidad de columnas: "))
filas = int(input("Ingrese la cantidad de filas: "))

matriz = []
valor = 1 

for i in range(columnas): # Generacion de matriz
    fil = [] 
    for o in range(filas):
        fil.append(valor)
        valor += 1
    matriz.append(fil)


matriz_trans = []
for i in range(columnas): # Matriz transpuesta
    fil = [] 
    for j in range(filas):
        fil.append(matriz[j][i])
    matriz_trans.append(fil)

print(f"La matriz original: {matriz}.")
print(f"La matriz transpuesta: {matriz_trans}.")