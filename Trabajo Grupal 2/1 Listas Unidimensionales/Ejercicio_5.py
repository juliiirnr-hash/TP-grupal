
#[ Ejercicio 5 ]:

lista = [1,2,5,10]


print(f"Lista inicial: {lista}")
mult = int(input("[Ingrese un numero multiplicador]:"))

for i in range(4):
    lista[i] *= mult


print(f"Lista final: {lista}")