#TP Listas de una dimensión  
#Ejercicio 9: Lista de Números Primos 
#Escribe un programa que permita al usuario ingresar una lista de números y filtre los números primos. 
from sympy import isprime #funcion para verificar si el numero es primo

Lista=list() 
while True:
    cantidad=int(input("Ingrese la cantidad de numeros que desea ingresar: ")) 
    if cantidad>0:
        break
    else:
        continue

for i in range(cantidad): 
    numeros = int(input(f"Ingrese numero [{i+1}]: "))
    Lista.append(numeros) 

Numeros_Primos=set() #Filtrara los numeros primos repetidos
for numeros in Lista:
  if isprime(numeros):
      Numeros_Primos.add(numeros)

if len(Numeros_Primos)>0:
    print(f"Numeros Primos:{Numeros_Primos}")
else:
    print("No hay numeros primos")   
   


