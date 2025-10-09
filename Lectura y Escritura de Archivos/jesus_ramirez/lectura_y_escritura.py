def leer_alumnos(direccion_archivo, alumnos, contenido):
    contenido_bruto = []
    contenido = []
    alumnos = {}
    try:
        with open(direccion_archivo, "r") as file:
            contenido_bruto = file.read().splitlines()

        for i in range(len(contenido_bruto)):
            contenido.append(contenido_bruto[i].split(";"))

            contenido[i][2] = int(contenido[i][2])
            contenido[i][3] = float(contenido[i][3])

            alumnos.update({int(contenido[i][2]): contenido[i][0]+" "+contenido[i][1]})

        print()
        return alumnos, contenido

    except FileNotFoundError:
        print("No se encontró el archivo. Creando uno...")
        with open(direccion_archivo, "x") as file:
            file.write("")


def agregar_alumno(direccion_archivo, alumnos, contenido):
    alumnos, contenido = leer_alumnos(direccion_archivo, alumnos, contenido)

    try:
        nombre = input("Nombre: ")
        if nombre == "" or nombre == " " or ";" in nombre:
            print("No permitido.")
            print()
            return None

        apellido = input("Apellido: ")
        if apellido == "" or apellido == " " or ";" in nombre:
            print("No permitido.")
            print()
            return None

        legajo = int(input("Legajo: "))
        if legajo < 10000 or legajo > 99999:
            print("El número está fuera de rango.")
            print()
            return None

        if validar_existe_alumno(alumnos, legajo):
            print()
            return None

        nota = float(input("Nota: "))
        if nota < 1 or nota > 10:
            print("El número está fuera de rango.")
            print()
            return True

    except ValueError:
        print("Valor inválido.")
        print()
        return None

    with open(direccion_archivo, "a") as file:
        file.write(f"{nombre};{apellido};{legajo};{nota}\n")


def validar_existe_alumno(alumnos, legajo):
    if legajo in alumnos.keys():
        print("Este legajo ya se encuentra en la lista.")
        return True


def guardar_aprobados(direccion_archivo, alumnos, contenido):
    alumnos, contenido = leer_alumnos(direccion_archivo, alumnos, contenido)

    with open("aprobados.txt", "w") as file:
        for i in range(len(contenido)):
            if contenido[i][3] >= 6:
                file.write(f"{contenido[i][0]};{contenido[i][1]};{contenido[i][2]};{contenido[i][3]}\n")

    with open("aprobados.txt", "r") as file:
        aprobados = file.read()
        print("Contenidos de aprobados.txt:")
        print(aprobados)


direccion_archivo = "alumnos.txt"
alumnos = {}
contenido = {}
while True:
    print("¿Qué quiere hacer?")
    decision = input("  [V]er alumnos.\n  [A]gregar alumno.\n  [G]enerar archivo de aprobados.\n  [S]alir.\n   ").lower()

    if decision == "v":
        alumnos, contenido = leer_alumnos(direccion_archivo, alumnos, contenido)
        for i in range(len(contenido)):
            print(contenido[i])
        print()

        for legajo, nombre in alumnos.items():
            print(f"{legajo}: {nombre}.")
        print()

    elif decision == "a":
        agregar_alumno(direccion_archivo, alumnos, contenido)

    elif decision == "g":
        guardar_aprobados(direccion_archivo, alumnos, contenido)

    elif decision == "s":
        break
    else:
        print("Inválido.")
