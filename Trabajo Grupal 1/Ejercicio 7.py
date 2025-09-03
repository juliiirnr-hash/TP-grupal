# Jesús Ramírez.
# 7- Solicite el ingreso de una cadena y determine el
# tamaño de la misma y cuantas vocales tiene en total.

# Creamos una clase para las cadenas que comprenda el
# texto y la cantidad de vocales.
class Cadena:
    def __init__(self, texto, vocales):
        self.texto = texto
        self.vocales = vocales

    # Creamos un método que pase carácter por carácter
    # contando cuántas vocales hay en el texto.
    def contador_de_vocales(self):
        for i in range(0, len(self.texto)):
            if self.texto[i] in ("a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"):
                self.vocales += 1
            else:
                pass

# Pedimos el valor de la variable frase y la añadimos
# a la clase Cadena. Luego ejecutamos el método para
# cambiar (o no) el valor de frase.vocales.
frase = Cadena(input("Escriba una cadena de caracteres. "),0)
frase.contador_de_vocales()

# Imprimimos por pantalla los valores de la variable.
print(f"La frase es: «{frase.texto}».")
print(f"Tiene una longitud de {len(frase.texto)} caracteres.")
print(f"Tiene una cantidad de {frase.vocales} vocales.")
