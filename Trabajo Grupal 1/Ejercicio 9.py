##Trabajo Practico Grupal Clases, Métodos y Parámetros 
#Ejercicio 9
#Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. 
#Muéstralos en línea recta, separados por un espacio entre cada carácter. 
texto="La lluvia en Mendoza es escasa"
ascii_codes = ' '.join(str(ord(letra)) for letra in texto)
#join: une los elementos de una lista en una cadena, usando el espacio como separador
#ord: devuelve el código ASCII de un carácter
#str: convierte un número en una cadena
#for letra in texto: recorre cada carácter de la cadena texto
print(ascii_codes)