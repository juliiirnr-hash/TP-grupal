#Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays
import numpy
# La libreria NumPy sirve para realizar operaciones matematicas y calculos mas complejos de forma mas eficiente
# en relacion con este trabajo, NumPy agrega herramientas para trabajar con arrays de una manera mas simplificada
# que nos evita usar bucles manuales y que el codigo se vuelva muy largo

import numpy as np


# por ejemplo, podriamos usamos este bloque para sumar dos listas...

lista1 = [1,2,3]
lista2 = [3,2,1]
listaSumados = []

for i in range(3):
   sumaElementos = lista1[i] + lista2[i]
   listaSumados.append(sumaElementos)

print(listaSumados)


# pero con NumPy se podria simplificar asi...

lista1 = numpy.array([1,2,3])
lista2 = numpy.array([3,2,1])

listaNumPy = lista1 + lista2

print(listaSumados)