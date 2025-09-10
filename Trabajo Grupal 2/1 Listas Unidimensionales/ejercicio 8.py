#TP Listas de una dimensión  
#Ejercicio 8:
# Encontrar Elementos Repetidos 
#Escribe un programa que identifique y muestre los elementos que se repiten en una lista. 
#Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los elementos. 
#Conjunto (set) es una estructura de datos que no permite elementos duplicados.
Lista=list() 
cantidad=int(input("Ingrese la cantidad de valores que desea ingresar: ")) 
for i in range(cantidad): 
    valores = input(f"Ingrese valor [{i+1}]: ") 
    Lista.append(valores) 
    
elementos_repetidos = set()
elementos_vistos = set() 
for valores in Lista:
    if valores in elementos_vistos: 
         elementos_repetidos.add(valores) #Si el valor ya ha sido visto, lo agregamos al conjunto de repetidos
    else: 
        elementos_vistos.add(valores) #Si no ha sido visto, lo agregamos al conjunto de vistos 
         
         
if len(elementos_repetidos) > 0: 
    print("Elementos repetidos:", elementos_repetidos) 
else: print("No hay elementos repetidos.")