# Ejercicio 4: - Desarrolle un programa que ayude a una cajera a determinar el número de billetes y monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de dinero dada. 
def Cambio(cantidad):
    
    denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]
    resultado = {}
    
    for valor in denominaciones:
        cantidadBilletes = int(cantidad // valor)
        if cantidadBilletes > 0:
            resultado[valor] = cantidadBilletes
            cantidad -= cantidadBilletes * valor
            cantidad = round(cantidad, 2)
    
    return resultado


cantidad = float(input("Ingrese la cantidad de dinero: "))

cambio = Cambio(cantidad)

print("Se necesitaran : ")
for valor, cantidadBilletes in cambio.items():
    if valor >= 1:
        print(f"{cantidadBilletes} billete(s) de ${int(valor)}")
    else:
        print(f"{cantidadBilletes} moneda(s) de ${valor:.2f}")