
# Practica Integradora

golosinas = [
    [1,  "KitKat",               20],
    [2,  "Chicles",              50],
    [3,  "Caramelos de Menta",   50],
    [4,  "Huevo Kinder",         10],
    [5,  "Chetoos",              10],
    [6,  "Twix",                 10],
    [7,  "M&M'S",                10],
    [8,  "Papas Lays",            2],
    [9,  "Milkybar",             10],
    [10, "Alfajor Tofi",         15],
    [11, "Lata Coca",            20],
    [12, "Chitos",               10],
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia",
}

clavesTecnico = ("admin","CCCDDD","2020")

golosinasPedidas = []

comando = ""

# ------------------------------------------------------ Funciones

def pedirGolosinas():
    legajo = int(input("[Ingrese su legajo]:"))
    if (legajo in empleados):
        while True:

            codigo = int(input("[Ingrese el codigo de golosina ( '0' para volver)]: "))

            if (codigo == 0 ): 
                break

            for golosina in golosinas:

                if(codigo in golosina and golosina[2] > 1):
                    print(f"Pidinedo {golosina[1]} . . .")

                    golosina[2] -= 1

                    agregarPedido(codigo)

                elif(codigo in golosina and golosina[2] < 1):
                    print("[!] Ya no nos queda de esa golosina")
            
            break

    else:
        print("[!] Usted no es empleado de la empresa")

def agregarPedido(codigo):
    for pedido in golosinasPedidas:
        if pedido[0] == codigo:
            pedido[2] += 1
            return

    for gol in golosinas:
        if gol[0] == codigo:
            golosinasPedidas.append([gol[0], gol[1], 1])
            return

def mostrarGolosinas():
    print("") 
    print("Golosinas Disponibles:") 
    for i in golosinas:
        print(i)

    print("")
    print(golosinasPedidas)

def rellenarGolosinas():

    for i in range(0,3):
        contra = input(f"[Ingresse contraseña {i+1}]:")
        if (contra != clavesTecnico[i]):
            print("[!] Contraseña incorrecta!")
            return

    print("")
    print("Autenticado completado")
    codigo = int(input("[Ingrese el codigo de una golosina]:"))

    while True:
        cantidad = int(input("[Ingrese la cantidad a agregar]:"))

        if(cantidad > 0):
            break
        else:
            print("la cantidad debe ser mayor a 0 ")

    for golo in golosinas:
        if (codigo in golo):
            golo[2] += cantidad
            return
    
    print("Esa golosina no existe")


# --------------------------------------------------------------- Main

while True:
    print("")
    print("---- MENU ------------")
    print("| a) Pedir Golosina")
    print("| b) Mostrar Golosina")
    print("| c) Rellenar Golosina")
    print("| d) Salir") 
    print("----------------------")

    print("")
    comando = input("[Elija una de las opciones anteriores]: ")
    print("")

    match comando:
        case "d":
            print("//// Fin programa ////")
            break
        case "a":
            pedirGolosinas()
        case "b":
            mostrarGolosinas()
        case "c":
            rellenarGolosinas()