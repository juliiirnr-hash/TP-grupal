# ACTIVIDAD 1: 
class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna 
        self.valor = valor
#Crear una matriz que contanga una variable celdas
class Matriz:
    def __init__(self):
        self.celdamatriz = []
#Agregar una nueva celda
    def agregar_celda(self, fila, columna, valor):
        for celda in self.celdamatriz:
            if celda.fila == fila and celda.columna == columna:
                print("Esa posición ya se encuentra cargada. Por favor intentelo nuevamente ")
                return 
        nueva_celda = Celda(fila, columna, valor)
        self.celdamatriz.append(nueva_celda)
#Mostrar celdas
    def mostrar_celdas(self):
        print("\n Celdas Cargadas: ")
        for celda in self.celdamatriz:
            print(f"Fila: {celda.fila}")
            print(f"Columna: {celda.columna}")
            print(f"Valor: {celda.valor}")
#Buscar valor
    def obtener_valor(self, fila, columna ):
        for celda in self.celdamatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y la columna indicada no ha sido asignada en ninguna celda"
    

def main():
    matriz = Matriz()

    while True:
        valor = input("Por favor ingrese un valor para la celda. O ingrese 'FIN' para terminar el programa: ")
        if valor.upper() == "FIN": 
            break
        
        if valor.strip() == "":
            print("Debe ingresar un valor")
            continue
        while True:
            try:
                fila = int(input("Por favor ingrese el número de fila: "))
                break
            except ValueError:
                print("Por favor ingrse un número: ")
        while True:
            try:
                columna = int(input("Por favor ingrese el número de columna: "))
                break
            except ValueError:
                print("Por favor ingrese un número: ")
        matriz.agregar_celda(fila,columna,valor)
    matriz.mostrar_celdas()
    
    buscar = input("\n¿Quiere buscar un valor en la matriz? s/si / n/no: ").lower()
    if buscar in ("s", "si"):
        while True:
            try:
                fila_buscar = int(input("Ingrese la fila que desea buscar: "))
                columna_buscar = int(input("Ingrese la columna que desea buscar: "))
                print(matriz.obtener_valor(fila_buscar, columna_buscar))
                break
            except ValueError:
                print("Por favor ingrese un número.")
    else: print("\nPrograma finalizado :)")

main()