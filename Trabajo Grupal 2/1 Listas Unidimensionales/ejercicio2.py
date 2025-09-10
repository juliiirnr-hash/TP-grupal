#Escribe un programa que pida al usuario una lista de números y encuentre el mayor y el menor de ellos.

numeros = []

cantidad = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(cantidad):
    num = float(input(f"Ingrese el número {i+1} :"))

    numeros.append(num)

print("El mayor número es: ", max(numeros))
print("El menor número es: ", min(numeros))
