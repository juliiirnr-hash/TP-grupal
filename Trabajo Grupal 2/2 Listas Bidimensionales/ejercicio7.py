#TP Listas Bidimensionales 
#Ejercicio7
#Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada.
matriz=[]
n=int(input("Ingrese el tamaño de la matriz identidad (n x n): "))
for i in range(n):
    fila = []  # lista vacía para cada fila
    for j in range(n):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)
for fila in matriz:
    print(fila)
#diagonal de la matriz ingresada
Diagonal=[]
for i in range(n):
    Diagonal.append(matriz[i][i])
print("La diagonal de la matriz es:", Diagonal)
