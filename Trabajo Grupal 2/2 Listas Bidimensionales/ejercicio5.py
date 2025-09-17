#Ejercicio 5: Escribe un programa que encuentre el valor más grande en una lista bidimensional.
lista = [
    [42, 53,78],
    [43, 7, 86],
    [6, 87, 64]
]

mayor = lista [0][0]

for fila in lista:
    for num in fila:
        if num > mayor:
            mayor = num


print("El valor más grande en la lista bidimensional es:", mayor)