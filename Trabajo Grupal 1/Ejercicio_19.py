
# [ EJERCICIO 19 ]:

class OperacionMatematica:
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2


    def sumarNumeros(self):
        return self.valor1 + self.valor2
    def restarNumeros(self):
        return self.valor1 - self.valor2
    def multiplicarNumeros(self):
        return self.valor1 * self.valor2
    def dividirNumeros(self):
        return self.valor1 / self.valor2
    
    def aplicarOperacion(self,operacion):
        match operacion:
            case "+":
                return self.sumarNumeros()
            case "-":
                return self.restarNumeros()
            case "*":
                return self.multiplicarNumeros()
            case "/":
                return self.dividirNumeros()
            case _:
                print("Opción no válida")


class Calculo:

    @staticmethod
    def main():
        operaciones = OperacionMatematica(8,2)

        print(operaciones.aplicarOperacion("+"))
        print(operaciones.aplicarOperacion("-"))
        print(operaciones.aplicarOperacion("*"))
        print(operaciones.aplicarOperacion("/"))

Calculo.main()