
# [ EJERCICIO 20 ]:

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    @staticmethod
    def sumarFracciones(f1, f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def restarFracciones(f1, f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def multiplicarFracciones(f1, f2):
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def dividirFracciones(f1, f2):
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        return Fraccion(num, den)


class OperacionesFraccion:

    @staticmethod
    def main():
        n1 = int(input("Numerador de la primera fracción: "))
        d1 = int(input("Denominador de la primera fracción: "))
        n2 = int(input("Numerador de la segunda fracción: "))
        d2 = int(input("Denominador de la segunda fracción: "))

        f1 = Fraccion(n1, d1)
        f2 = Fraccion(n2, d2)

        print(f"\nFracción 1: {f1}")
        print(f"Fracción 2: {f2}\n")

        suma = Fraccion.sumarFracciones(f1, f2)
        resta = Fraccion.restarFracciones(f1, f2)
        multi = Fraccion.multiplicarFracciones(f1, f2)
        div = Fraccion.dividirFracciones(f1, f2)

        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multi}")
        print(f"División: {div}")



OperacionesFraccion.main()