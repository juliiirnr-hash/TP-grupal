datosAlumnos= {}

# leo el archivo con with y cargo el diccionario con los datos del archivo
try:
    with open("alumnos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() == "":
                continue
            nombreAlumno, apellidoAlumno, legajoAlumno, notaAlumno = linea.strip().split(";")
            datosAlumnos[legajoAlumno] = {
                "nombre": nombreAlumno,
                "apellido": apellidoAlumno,
                "nota": notaAlumno}
except FileNotFoundError:
    # si no existe el archivo, lo creo vacío
    with open("alumnos.txt", "w", encoding="utf-8") as archivo:
        pass
except Exception as e:
    print("Error al leer el archivo:", e)


def verAlumnos():
    # muestra todos los alumnos del archivo
    if not datosAlumnos:
        print("\nNo hay alumnos cargados.\n")
        return

    for legajo, datos in datosAlumnos.items():
        print(" ")
        print(f"Legajo: {legajo}")
        print(f"Nombre: {datos['nombre']} {datos['apellido']}")
        print(f"Nota: {datos['nota']}")
        print(" ")


def agregarAlumnos():
    # agrega un nuevo alumno validando los datos antes de guardar
    print("\n--- Agregar nuevo alumno ---")

    # validación del nombre
    while True:
        nombre = input("Ingresa el nombre del alumno/a : ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        print("❌ El nombre solo puede contener letras.")

    # validación del apellido
    while True:
        apellido = input("Ingresa el apellido del alumno/a: ").strip()
        if apellido.replace(" ", "").isalpha():
            break
        print("❌ El apellido solo puede contener letras.")

    # validación del legajo
    while True:
        legajo = input("Ingresa el legajo (5 dígitos) del alumno/a: ").strip()
        if not (legajo.isdigit() and len(legajo) == 5):
            print("❌ El legajo debe tener 5 dígitos numéricos.")
            continue
        if legajo in datosAlumnos:
            print(f"❌ El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura.")
            return
        break

    # validación de la nota promedio
    while True:
        nota = input("Ingrese nota promedio (1-10): ").strip()
        if nota.replace('.', '', 1).isdigit():
            if 1 <= float(nota) <= 10:
                break
        print("❌ La nota debe ser un número entre 1 y 10.")

    # Agregar al diccionario
    datosAlumnos[legajo] = {
        "nombre": nombre,
        "apellido": apellido,
        "nota": nota
    }

    # Guardar en el archivo
    try:
        with open("alumnos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")
        print("✅ Alumno agregado correctamente.")
    except Exception as e:
        print("Error al escribir en el archivo:", e)


def verAprobados():
    # genera el archivo de alumnos aprobados (nota >= 6) y lo muestra por pantalla
    try:
        with open("aprobados.txt", "w", encoding="utf-8") as archivo:
            for legajo, datos in datosAlumnos.items():
                try:
                    if float(datos["nota"]) >= 6:
                        archivo.write(f"{datos['nombre']};{datos['apellido']};{legajo};{datos['nota']}\n")
                except ValueError:
                    continue

        print("\n--- ALUMNOS APROBADOS ---")
        with open("aprobados.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if contenido:
                print(contenido)
            else:
                print("No hay alumnos aprobados.")
        print("--------------------------")
    except Exception as e:
        print("Error al generar el archivo aprobados.txt:", e)


# menú principal del programa
while True:
    seleccionMenu = input(print("\n1)Ver alumnos \n2)Añadir alumno \n3)Ver alumnos aprobados \n4)salir"))

    match seleccionMenu:
        case "1":
            verAlumnos()
        case "2":
            agregarAlumnos()
        case "3":
            verAprobados()
        case "4":
            print("salir")
            break
        case _:
            print("Ingrese una opcion valida")
