# Jesús Ramírez.
# 8- Reemplaza todas las vocales a de una cadena
# ingresada por teclado por una vocal e.

# Creamos una clase que contenga el texto original
# y el cambiado.
class Cadena:
    def __init__(self, original, cambiada):
        self.original = original
        self.cambiada = cambiada

    # Creamos un método que pase carácter por carácter
    # cambiando las "a"s a "e"s cada que detecte una.
    def cambio_de_vocal(self):
        for i in range(0, len(self.original)):
            if self.original[i] == "a" or self.original[i] == "á":
                self.cambiada += "e"
            else:
                self.cambiada += self.original[i]

# Le asignamos un valor introducido por el usuario a
# variable e inicializamos el método para luego
# mostrar la conversión por pantalla.
frase = Cadena(input("Escriba una cadena de caracteres. "),"")
frase.cambio_de_vocal()
print(frase.cambiada)
