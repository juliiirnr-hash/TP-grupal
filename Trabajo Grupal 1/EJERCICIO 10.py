##Trabajo Practico Grupal Clases, Métodos y Parámetros 
#Ejercicio 10
#Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario  pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el resultado por pantalla.  
palabra=input("Ingrese una palabra o frase: ")
opcion=input("Ingrese 'may' para convertir a mayúscula o 'min' para convertir a minúscula: ").lower()


if opcion=="may":
     print(palabra.upper())
     #upper: convierte una cadena a mayúsculas
elif opcion=="min":
      print(palabra.lower())
      #lower: convierte una cadena a minúsculas
else:
     print("Opción no válida. Por favor, ingrese 'May' o 'min'.")
     

