#TP Listas de una dimensión  
#Ejercicio 10: Eliminar un Elemento por su Índice
#Escribe un programa que permita al usuario ingresar una lista de números y eliminar un elemento en un índice especificado. 
Lista=list() 
while True:
    cantidad=int(input("Ingrese la cantidad de numeros que desea ingresar: ")) 
    if cantidad>0:
        break
    else:
        print("La cantidad de numeros debe ser mayor a cero")
        continue
for i in range(1,cantidad+1): 
    a= input(f"Ingrese valor [{i}]: ")
    Lista.append(a) 

c=0
decision=input("Desea eliminar un elemento(s para elimanar elemento u otro para no modificarlo): ").lower()

if decision =="s":
     while True:
         indice=int(input("Ingrese el índice del elemento que desea eliminar: "))
         c+=1
         if 1<=indice<=len(Lista):
            del Lista[indice-1]
            
         else:
            print("Por favor, ingrese un índice que exista dentro de la lista!!")
            continue 
         if c==1:
             break

       
print(Lista)
