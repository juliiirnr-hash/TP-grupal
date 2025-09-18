# Una empresa de software les brinda a sus empleados como parte de sus
# beneficios la posibilidad de acceder de forma gratuita a una máquina de
# Golosinas. Nuestra tarea será la programación de las funcionalidades
# necesarias para llevar adelante este beneficio.

# La lista "golosinas" contiene la información sobre los productos de la máquina.
# La primera columna indica el número que identifica el producto, la segunda
# muestra el nombre del producto y la tercera las unidades del producto disponibles.
            # Número, Nombre, Cantidad.
golosinas = [[1, "KitKat", 20],
             [2, "Chicles", 50],
             [3, "Caramelos de Menta", 50],
             [4, "Huevo Kinder", 10],
             [5, "Chetoos", 10],
             [6, "Twix", 10],
             [7, "M&M's", 10],
             [8, "Papas Lays", 2],
             [9, "Milkybar", 10],
             [10, "Alfajor Tofi", 15],
             [11, "Lata Coca", 20],
             [12, "Chitos", 10]]

# El diccionario "empleados" contiene, en la primera columna, el legajo de los
# empleados y, en "la segunda, los nombres asociados.
            # Legajo: Nombre Completo.
empleados = {"1100": "José Alonso",
             "1200": "Federico Pacheco",
             "1300": "Nelson Pereira",
             "1400": "Osvaldo Tejada",
             "1500": "Gastón Garcia"}

# "clavesTecnico" contiene las tres palabras clave para poder añadir unidades a
# los productos de "golosinas".
clavesTecnico = ("admin", "CCCDDD", "2020")

# Creamos e inicializamos algunas variables importantes antes del bucle para
# minimizar errores y agilizar la lectura de sus líneas internas.
golosinasPedidas = [] # Contendrá información sobre los productos seleccionados por el usuario.
opcion = False # Será utilizada para la condición del bucle.
empleadoVerificado = False # Se inicia acá para volverla inmune a los cambios internos del bucle.
totalPedido = 0
while opcion != "d" and opcion != "D": # El valor de "opcion" empieza en "False".
    opcion = input("Elija:\n a) Pedir golosina.\n b) Mostrar golosinas.\n c) Rellenar golosinas.\n d) Apagar máquina.\n ")
    print() # Preguntamos qué acción realizar cada vez que empiece el bucle.
    numeroPedido = None # Servirá para identificar algún producto en "golosinas".
    cantidad = None # Servirá para indicar la cantidad de unidades a operar.
    golosinaYaRetirada = False

    # Opción A. Pide productos de la máquina.
    if opcion == "a" or opcion == "A":
        if empleadoVerificado == False: # Ahorra el ingreso del legajo cada que se entra en la opción.
            legajo = input("Ingrese su legajo: ")
            if legajo not in empleados: # Pide el legajo. Si no se encuentra en "empleados", fuerza el programa a finalizar.
                print("Usted no se encuentra en la lista de empleados de la empresa.")
                break
            print(f"Bienvenido, {empleados[legajo]}.") # Saca el nombre del empleado para darle un corto saludo.
        empleadoVerificado = True # Se cambia el valor de "empleadoVerificado" para ahorranos las condicionales anteriores.

        # Pide el identificador de la golosina y verifica el valor ingresado:
        # si es inválido, vuelve al menú principal; si no lo es, continúa.
        numeroPedido = int(input("Código de la golosina: "))
        if numeroPedido < 0 or numeroPedido > 12:
            print("El valor no representa a ninguna golosina. ")
            print()
            continue

        # Pregunta por la cantidad de productos a extraer y verifica que no
        # excedan el máximo, sean cero o resulten ser negativos.
        cantidad = int(input(f"Unidades de {golosinas[numeroPedido-1][1]}: "))
        if cantidad < 1 or cantidad > golosinas[numeroPedido-1][2]:
            print("La cantidad ingresada está por debajo de uno o por encima de la almacenada. No se puede. ")
            print()
            continue
        # Una vez se validada la cantidad, se revisa si el producto ya ha sido
        # pedido antes: si sí, tan sólo se aumenta la cantidad de unidades; si
        # no, se añade una línea nueva. Pase lo que pase, reduce la cantidad de
        # "golocinas" de forma acorde.
        for i in range(0, len(golosinasPedidas)):
            if golosinas[numeroPedido-1][1] not in golosinasPedidas[i][1]:
                pass
            else:
                golosinasPedidas[i][2] += cantidad
                golosinas[numeroPedido-1][2] -= cantidad
                golosinaYaRetirada = True
                break
        if golosinaYaRetirada != True:
            golosinasPedidas.append([golosinas[numeroPedido-1][0], golosinas[numeroPedido-1][1], cantidad])
            golosinas[numeroPedido-1][2] -= cantidad
        print()

    # Opción B. Muestra por pantalla la lista entera de productos en un bucle.
    # Esta lista se actualiza, no es estática.
    elif opcion == "b" or opcion == "B":
        for i in range(0,len(golosinas)):
            for j in range(0,len(golosinas[0])):
                print(golosinas[i][j], end='  ')
            print()
        print()
        continue

    # Opción C. Abastece "golosinas" de más unidades.
    elif opcion == "c" or opcion == "C":
        # Pide las tres claves de "clavesTecnico".
        claveTecnico1 = input("Primera clave: ")
        claveTecnico2 = input("Segunda clave: ")
        claveTecnico3 = input("Tercera clave: ")

        # Si no coinciden, se rompe el bucle y finaliza el programa.
        if claveTecnico1 != clavesTecnico[0] and claveTecnico2 != clavesTecnico[1] and claveTecnico3 != clavesTecnico[2]:
            print("Claves inválidas. Usted no tiene permiso para hacer recargas. ")
            break

        # Si coinciden, se pregunta el número del producto. Luego se comprueba
        # su validez y usa como referencia para añadir unidades.
        numeroPedido = int(input("Código de la golosina: "))
        if numeroPedido < 0 or numeroPedido > 12:
            print("El valor no representa a ninguna golosina. ")
            print()
            continue

        # Pregunta por las unidades del producto a añadir, comprueba su validez
        # y se añaden al mismo.
        cantidad = int(input(f"Unidades de {golosinas[numeroPedido-1][1]} añadidas: "))
        if cantidad <= 0:
            print("Valor inválido. No se puede añadir cero o menos de cero. ")
            print()
            continue
        golosinas[numeroPedido-1][2] += cantidad

    # Opción D. Salir del programa. Si el valor de "golosinasPedidas" no está
    # vacío, imprime sus contenidos por pantalla con un bucle for.
    elif opcion == "d" or opcion == "D":
        if golosinasPedidas == []:
            break

        print("Usted ha pedido:")
        for i in range(0,len(golosinasPedidas)):
            totalPedido += golosinasPedidas[i][2]
            for j in range(0,len(golosinasPedidas[0])):
                print(golosinasPedidas[i][j], end='  ')
            print()
        print(f"Total: {totalPedido}.")
        print()

    # En caso de que no haya sido ninguno de los anteriores, se hará saber y repetirá la pregunta.
    else:
        print("Valor inválido.")
        print()
