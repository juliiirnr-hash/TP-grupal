
# [ Ejercicio 3 ]:

columnas = int(input("Ingrese la cantidad de columnas: "))
filas = int(input("Ingrese la cantidad de filas: "))

matriz = []
valor = 1 

for i in range(columnas):
    fil = [] 
    for o in range(filas):
        fil.append(valor)
        valor += 1
    matriz.append(fil)

print(f"La matriz es: {matriz}.")


total = 0
for i in range(columnas):
    print(f"[Total fila {i+1}]: {sum(matriz[i])}")

print(f"El total de la matriz es {total}.")