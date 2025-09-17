#practica integradora individual

#matriz que contiene los datos Codigo,Golosinas y Sotck disponible

golosinas = [[1,"Kitkat",20],[2,"Chicles",50], [3,"Caramelos de Menta",50],
             [4,"Huevo Kinder",10],[5,"Chetoos",10],
             [6,"Twix",10],[7,"M&M's",10],[8,"Papas Lays",2],[9,"Milky bar",10],
             [10,"Alfajor Tofi",15],[11,"Lata Coca",20],[12,"Chitos",10]]

#diccionario que contiene el Legajo y Nombre del empleado
empleados = {1100:"José Alonso", 1200:"Federico Pacheco",
1300:"Nelson Pereira", 1400:"Osvaldo Tejada", 1500:"Gaston Garcia",}

#tupla para almacenar las claves de tecnicos
clavesTecnicos = ("admin","CCCDDD","2020")

#lista de golosinas pedidas
golosinasPedidas = [[1,"Kitkat",0],[2,"Chicles",0],[3,"Caramelos de Menta",0],[4,"Huevo kinder",0],
                    [5,"Chetoos",0],[6,"Twix",0],[7,"M&M's",0],[8,"Papas Lays",0],[9,"Milky bar",0],
                    [10,"Alfajor Tofi",0],[11,"Lata Coca",0],[12,"Chitos",0]]

#funcion para pedir golosina
def pedirGolosina():
    sublistasGolosinas = None
    sublistasGPedidas = None

    legajoIngresado = int(input("Ingrese su legajo de empleado: \n"))

    if legajoIngresado in empleados:
        golosinaIngresada = int(input("Ingresa el codigo de la golosina a pedir:\n"))
    #encontrar la fila o subarreglo q contenga la golosina a pedir
        for g in golosinas:
            if g[0] == golosinaIngresada:
                sublistasGolosinas = g
                break
    #pedir la cantidad
        cantidadAPedir = int(input(f"Cuantas unidades de {sublistasGolosinas[1]} solicita?:\n"))

        if sublistasGolosinas is not None:
    #restar del stock
            if sublistasGolosinas[2] >= cantidadAPedir:
                sublistasGolosinas[2] -= cantidadAPedir
            else: print("No queda stock suficiente de la golosina solicitada")
    #agregar a la lista de golosinas pedidas

            for gp in golosinasPedidas:
                if gp[1] == sublistasGolosinas[1]:
                    sublistasGPedidas = gp
                    break
            sublistasGPedidas[2] += cantidadAPedir
            
            print (f"Usted solicitó {cantidadAPedir} ,quedan {sublistasGolosinas[2]} unidades en stock")
        else: 
            print("Ya no queda stock de la golosina ingresada o el codigo ingresado es incorrecto")
    else:
        print("el legajo ingresado no pertenece a un empleado en esta empresa")

#funcion para mostrar golosinas

def mostrarGolosinas():
    for g in golosinas:
        print(f" {g[0]}| {g[1]}: {g[2]} unidades")

#funcion para rellenar golosinas

def rellenarGolosinas():

    inicioTecnico = input("Inicie sesión ingresando los datos en formato: usuario contraseña año\n")
    datosTecnico = inicioTecnico.split()

    if len(datosTecnico) == 3:
        usuario, contrasenia, anio = datosTecnico
        if (usuario,contrasenia,anio) == clavesTecnicos:
                
                golosinasARellenar = int(input("Ingrese el codigo de la golosina rellenar:\n"))
                #buscar la golosina
                for g in golosinas:
                    if g[0] == golosinasARellenar:
                        sublistasGolosinas = g
                        break
                #pedir la cantidad 
                if sublistasGolosinas is not None:
                    cantidadARellenar = int(input(f"Cuantas unidades de {sublistasGolosinas[1]} solicita?:\n"))
                    sublistasGolosinas[2] += cantidadARellenar
                    print(f"Se rellenaron {cantidadARellenar} unidades de {sublistasGolosinas[1]}")
                    print(f"El stock actual de {sublistasGolosinas[1]} es de: {sublistasGolosinas[2]}")
                else:
                    print("Código de golosina incorrecto")
        else:
            print("Los datos ingresados no corresponden a ningun tecnico de la empresa")
    else:
        print("Formato incorrecto")
        


#funcion para apagar maquina

def apagarMaquina():
    for gp in golosinasPedidas:
        print(f" {gp[0]}| {gp[1]}: {gp[2]} unidades solicitadas hoy")

#imprimo el inicio
while True:

    indiceInicio = input("------------------------------------\n¿Que desea hacer?:\n" \
    "a.Pedir golosina\nb.Mostrar golosina\nc.Rellenar golosina\nd.Apagar maquina\n------------------------------------\n")

#match case para el inicio
    match indiceInicio:
        case "a":
            pedirGolosina()
        case "b":
            mostrarGolosinas()
        case "c":
            rellenarGolosinas()
        case "d":
            apagarMaquina()
            break
        case _:
            print ("No es una opción valida, intente de nuevo...")
