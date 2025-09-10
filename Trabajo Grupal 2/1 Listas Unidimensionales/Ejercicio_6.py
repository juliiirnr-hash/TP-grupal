
#[ Ejercicio 6 ]:

lista = []

print("[Vamos a llenar una lista de 5 elementos]")
for i in range(5):
    lista.append(int(input("[Ingrese nuevo numero para la lista]:")))

print(f"Lista inicial: {lista}")

lista = list(set(lista))

print(f"Lista final: {lista}")