#ejercicio 11

longitudLista = int(input("Ingresa el tamaño de la lista (solo carácteres numerales): "))
lista = []

for i in range(longitudLista):
    elementosLista = input(f"Ingresa el elemento {i+1} de la lista: ")
    lista.append(elementosLista)

numeroRepeticiones = (input("Ingresa un caracter para ver cuantas veces se repite en la lista : "))
repeticiones = lista.count(numeroRepeticiones)
if repeticiones == 1: print("El caracter no se repite")
elif repeticiones == 0: print("El caracter no está en la lista")
else:
    print(f"El caracter se repite {repeticiones} veces.")