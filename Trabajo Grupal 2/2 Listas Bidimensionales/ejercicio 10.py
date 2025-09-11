#ejercicio 10
import numpy as np
#solicito una matriz

n = int(input("Ingrese el tamaño de la matriz para luego verificar si es simetrica: "))
matrizSimetrica=[]
for i in range(n):
    fila=[]
    for j in range(n):
        elementoMatriz=(input(f"ingresa elemento de la posicion [{j+1},{i+1}]: "))
        fila.append(elementoMatriz)
    matrizSimetrica.append(fila)

#lo transformo en un array de numpy
matrizSimetrica = np.array(matrizSimetrica)

#recibo la transpuesta con .t y verifico si es simetrica con array_equal

if np.array_equal(matrizSimetrica, matrizSimetrica.T):
    print(f"La matriz\n {matrizSimetrica} \nEs simetrica.")
else:
    print(f"La matriz\n {matrizSimetrica} \nNo es simetrica.")