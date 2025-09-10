lista = []

# Pedimos el tamaño de la lista.
cantidad = int(input("¿Cuántos valores quiere en su lista? "))

contadorPar = 0
contadorImpar = 0
# Dejamos que el usuario indique el valor de cada instancia; dependiendo en si
# es par o impar, se cuenta en una variable distinta.
for i in range(cantidad):
    lista.append(int(input(f"Valor de {i}: ")))
    if lista[i] % 2 == 0:
        contadorPar += 1
    else:
        contadorImpar += 1
print(lista)

print(f"Cantidad de números pares: {contadorPar}.")
print(f"Cantidad de números impares: {contadorImpar}.")
