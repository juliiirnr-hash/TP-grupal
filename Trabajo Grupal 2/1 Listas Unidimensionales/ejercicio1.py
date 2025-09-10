7#Escribe un programa que permita al usuario ingresar una lista de números y calcule la suma de todos los elementos en la lista.

numeros = []

print("Ingrese números separados por un espacio, para finalizar el ingreso de números escriba la palabra 'fin'")

while True:
    entrada = input("Número: ") #pedimos al usuario que ingrese los números
    if entrada.lower() == "fin": #Utilizamos lower(), donde convierte los caracteres a minuscula, para que no afecte el como ingrese la palabra el usuario
        break
 
    numero = float(entrada)  
    numeros.append(numero) #con .append guardaremos dentro de la lista los números que el usuario ingrese
    

suma_total = sum(numeros)

print("La suma de todos los elementos es:", suma_total)
