#1)La lista de 2 dimensiones de las golosinas
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

# 2) Diccionario de empleados 
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

#3) TUPLA: Claves del técnico
clavesTecnico = ("admin", "CCCDDD", "2020")

golosinasPedidas = []

#Funciones para el menú principal 
# a) pedir golosina


def pedir_golosina():
    try:
        legajo = int(input("Ingrese su legajo: "))
    except ValueError:
        print("El legajo ingresado es incorrecto.")
        return

    if legajo not in empleados:
        print("Usted no es un empleado de la empresa.")
        return

    print(f"Bienvenido {empleados[legajo]} :) ")
    mostrar_golosinas()

    while True:
        try:
            codigo = input("Ingrese el código de la golosina (o escriba 'volver' para volver al menú principal): ")
            if codigo.lower() == "volver":
                return
            codigo = int(codigo)
        except ValueError:
            print("El código ingresado es invalido")
            continue

        golosina1 = next((g for g in golosinas if g[0] == codigo), None)

        if golosina1:
            if golosina1 [2] > 0:
                golosina1 [2] -= 1
                print(f"Usted ha pedido {golosina1[1]}.")
                pedido = next((p for p in golosinasPedidas if p[0] == codigo), None)
                if pedido:
                    pedido[2] += 1
                else:
                    golosinasPedidas.append([codigo, golosina1[1], 1])
            else:
                print(f"La golosina {golosina1[1]} no tiene stock :(.")
        else:
            print("Código incorrecto.")

# b) mostrar golosina
def mostrar_golosinas():
    print("\n Golosinas disponibles:")
    for codigo, nombre, stock in golosinas:
        print(f"Código: {codigo:2} | {nombre:15} | Stock: {stock}")
    print("-" * 40)

# c) rellenar golosinas
def recargar_golosinas():
    print("Ingreso de técnico requerido.")
    claves = []
    for i in range(3):
        clave = input(f"Ingrese la clave {i + 1}: ")
        claves.append(clave)

    if tuple(claves) != clavesTecnico:
        print("No cuenta con el permiso para ejecutar la recarga.")
        return

    try:
        codigo = int(input("Ingrese el código de la golosina a recargar: "))
        cantidad = int(input("Ingrese la cantidad a recargar: "))
    except ValueError:
        print("Valores inválidos. :( ")
        return

    if cantidad <= 0:
        print("La cantidad a ingresar debe ser mayor a 0.")
        return

    golosina2 = next((g for g in golosinas if g[0] == codigo), None)
    if golosina2:
        golosina2 [2] += cantidad
        print(f"Recargo {cantidad} unidades de {golosina2[1]}. Stock actual: {golosina2[2]}")
    else:
        print("Código inexistente :(.")

# d) apagar la maquina
def apagar_maquina():
    print("\n Historial de golosinas pedidas:")
    total = 0
    for codigo, nombre, cantidad in golosinasPedidas:
        print(f"Código: {codigo:2} | {nombre:15} | Pedidas: {cantidad}")
        total += cantidad
    print(f"\n Total de golosinas pedidas: {total}")
    print("Maquina apagada :) ")


def menu():
    while True:
        print("\n MENÚ PRINCIPAL: ")
        print("a) Pedir golosina")
        print("b) Mostrar golosinas")
        print("c) Rellenar golosinas ")
        print("d) Apagar máquina")
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            pedir_golosina()
        elif opcion == "b":
            mostrar_golosinas()
        elif opcion == "c":
            recargar_golosinas()
        elif opcion == "d":
            apagar_maquina()
            break
        else:
            print("Opción incorrecta, intentelo nuevamente :( ")

menu()
