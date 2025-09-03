#Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique
#Primer ejemplo: Se asigna un valor entero fuera de rango.
valorEntero = 9999999999999999999999999999999999999
print(f"Entero: {valorEntero}")
#En este caso se puede llevar cabo sin ningun problema.
#Segundo ejemplo: flotante con un valor fuera de rango.
#valor máximo de almacenamiento:
valorFloat = 1.79e308   
#valor fuera de rango:
valorFuera = 1.8e308 
print("Valor dentro de rango:", valorFloat)
print("Valor fuera de rango:", valorFuera)  
#Al ser un valor fuera de rango en la salida se convierte en infinito "(inf)""

#solución:

if valorFuera == float("inf"):
    print("El número esta fuera de rango")