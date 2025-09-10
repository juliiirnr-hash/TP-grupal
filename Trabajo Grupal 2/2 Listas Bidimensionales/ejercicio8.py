#TP Listas Bidimensionales 
#Ejercicio 8: Matriz Identidad 
#Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto son 0
#matriz identidad de tamaño n x n
#donde n es un número ingresado por el usuario
#y la matriz identidad es una matriz cuadrada en la que todos los elementos de la diagonal

n = int(input("Ingrese el tamaño de la matriz identidad (n x n): "))
identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for fila in identidad:
 print(fila)