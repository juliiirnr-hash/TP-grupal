
#[ Ejercicio 7 ]:

# este ejercicio se puede resolver sin usar listas,
# sumando y contando las entradas del usuario.
# PERO, voy a usar listas ya que es relevante al practico


lista = []

print("[Vamos a llenar una lista, agregue 0 para terminar")

entrada = 1 

while True:
    entrada = int(input("[Ingrese siguiente valor]:"))
    if (entrada == 0):
        break
    lista.append(entrada)
    

print(f"El promedio es de {sum(lista) / len(lista)}")