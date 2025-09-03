# Jesús Ramírez.
# 5. Solicite el ingreso de una cadena y elimine todos los
# espacios de la misma, muestre la cadena resultante.

# Definimos una clase llamada Cadena, que contendrá tanto
# el texto ingresado por el usuario como el procesado.
class Cadena:
    def __init__(self, ingresado, procesado):
        self.ingresado = ingresado
        self.procesado = procesado

    # Definimos el método en que verifique, carácter por
    # carácter, si hay espacios: si hay, la versión procesada
    # los omite y copia el resto del texto.
    def remocion_de_espacios(self):
        for i in range(0, len(self.ingresado)):
            if self.ingresado[i] == " ":
                pass
            else:
                self.procesado += self.ingresado[i]

# Pedimos el texto al usuario.
frase = Cadena(input("Escriba una cadena de caracteres. "),"")
#Ejecutamos el método de remoción y luego imprimimos el resultado.
frase.remocion_de_espacios()
print(frase.procesado)
