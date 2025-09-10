#ejercicio 12
longitudLista = int(input("Ingresa el tamaño de las listas (solo carácteres numerales): "))

lista1 = []
lista2 = []

for i in range(longitudLista):
    while True:
        try:
            elementosLista1 = int(input(f"Ingresa el numero en posicion {i+1} de la primer lista: "))
            lista1.append(elementosLista1)
            break
        except ValueError:
            print("El elemento ingresado no es un numero,intentá nuevamente")

print("")

for i in range(longitudLista):
    while True:
        try:
            elementosLista2 = int(input(f"Ingresa el numero en posicion {i+1} de la segunda lista: "))
            lista2.append(elementosLista2)
            break
        except ValueError:
            print("El elemento ingresado no es un numero,intentá nuevamente")

listaSumados = []

for i in range(longitudLista):
   sumaElementos = lista1[i] + lista2[i]
   listaSumados.append(sumaElementos)



print(listaSumados)