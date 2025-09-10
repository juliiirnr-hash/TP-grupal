lista = []

# Pedimos el tamaño de la lista.
cantidad = int(input("¿Cuántos valores quiere en su lista? "))

# Dejamos que el usuario indique el valor de cada instancia.
for i in range(cantidad):
    lista.append(input(f"Valor de {i}: "))

# Mostramos la lista ingresada, la revertimos y remostramos.
print(f"Usted ingresó {lista}.")
lista.reverse()
print(f"Se invirtió a {lista}.")
