#ejercicio 9
import numpy as np

#solicito el tamaño 'n' para la matriz
n = int(input("Ingresa el tamaño que quieres que tenga la matriz identidad inversa: "))

#con la bibilioteca de numpy uso .eye  para crear la matriz y voltearla con fliplr
matrizInversa= np.fliplr(np.eye(n))

print(matrizInversa)
