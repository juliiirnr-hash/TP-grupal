#Ejercicio 3: Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 efectué la suma de los 3 dígitos del número.
num = int(input("Ingrese un número de 3 digitos: "))
digito1 = num % 10
num = num // 10
digito2 = num % 10
num = num // 10
digito3 = num % 10

suma = digito1 + digito2 + digito3

print(f"Suma de los tres dígitos del número ingresado: {suma}")