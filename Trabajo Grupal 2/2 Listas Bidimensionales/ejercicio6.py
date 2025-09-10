#Ejercicio 6 : Escribe un programa que multiplique cada elemento de una lista bidimensional por un valor escalar dado por el usuario.

filas = int(input("Ingrese el número de filas que tendrá la lista: "))
columnas = int(input("Ingrese el número de columnas que tendrá la lista: "))


matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)


escalar = int(input("\nIngrese el valor escalar para multiplicar: "))

matrizResultado = []
for fila in matriz:
    nueva_fila = []
    for num in fila:
        nueva_fila.append(num * escalar)
    matrizResultado.append(nueva_fila)


print("\nMatriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz resultante después de multiplicar por", escalar, ":")
for fila in matrizResultado:
    print(fila)