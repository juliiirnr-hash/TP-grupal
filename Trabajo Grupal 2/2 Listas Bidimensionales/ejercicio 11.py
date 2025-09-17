import numpy as np

#solicito la matriz
n = int(input("Ingrese el tamaño de la matriz para luego rotarla: "))
matrizARotar=[]
for i in range(n):
    fila=[]
    for j in range(n):
        elementoMatriz=(input(f"ingresa elemento de la posicion [{j+1},{i+1}]: "))
        fila.append(elementoMatriz)
    matrizARotar.append(fila)

#lo transformo a un array de numpy
matrizARotar = np.array(matrizARotar)

#la roto a 90° con rot90 y selecciono la direccion (sentido horario) con k -1
matrizRotada = np.rot90(matrizARotar, k=-1)
print(matrizRotada)

