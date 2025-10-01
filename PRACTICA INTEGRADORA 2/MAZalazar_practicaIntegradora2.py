# gestionNotas

# Diccionario "Alumnos" (legajo y nombre)
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomes",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# Matriz "Materias"
materias = [
    ["Ciencias", "", "", "", ""],
    ["Historia", "", "", "", ""],
    ["Geografia", "", "", "", ""],
    ["Matematicas", "", "", "", ""],
    ["Fisica", "", "", "", ""]
]

# Lista "Notas finales" (nombre del alumno, promedio general)
notasFinales = [
    ["Rodolfo Fernandez", ""],
    ["Luis Gomes", ""],
    ["Andrea Pereira", ""],
    ["Juan Cruz Gonzales", ""]
]

# Lista de nombres de alumnos para ubicar índices en notasFinales
nombres = list(alumnos.values())

# Variable para almacenar el mejor promedio general
mejor_promedio = -1
mejor_alumno = ""

# Iterar sobre los alumnos
for legajo, nombreAlumno in alumnos.items():
    print(f"\nIngresando notas para el alumno {nombreAlumno}:")

    suma_promedios = 0  # Para calcular promedio general del alumno

    # Iterar sobre las materias
    for i, materia in enumerate(materias):
        print(f"\nMateria: {materia[0]}")

        # Ingreso de nota 1
        while True:
            try:
                nota1 = float(input("Ingrese la nota 1 (0-10): "))
                if 0 <= nota1 <= 10:
                    break
                else:
                    print("Dato ingresado no válido. Debe estar entre 0 y 10.")
            except ValueError:
                print("Dato ingresado no válido. Debe ser un número.")

        # Ingreso de nota 2
        while True:
            try:
                nota2 = float(input("Ingrese la nota 2 (0-10): "))
                if 0 <= nota2 <= 10:
                    break
                else:
                    print("Dato ingresado no válido. Debe estar entre 0 y 10.")
            except ValueError:
                print("Dato ingresado no válido. Debe ser un número.")

        # Calcular promedio de la materia
        promedio = (nota1 + nota2) / 2
        print(f"Nota Final: {promedio:.2f}")

        # Guardar notas y promedio en la matriz
        # Nota1 -> columna 1, Nota2 -> columna 2, Promedio -> columna 3
        materia[1] = nota1
        materia[2] = nota2
        materia[3] = promedio

        # Sumar para el promedio general
        suma_promedios += promedio

    # Determinar materia con la calificación más alta
    mejor_materia = max(materias, key=lambda x: x[3])
    print(f"\nMateria con mejor calificación de {nombreAlumno}: {mejor_materia[0]} con {mejor_materia[3]:.2f}")

    # Calcular promedio general del alumno
    promedio_general = suma_promedios / len(materias)
    print(f"Promedio general de {nombreAlumno}: {promedio_general:.2f}")

    # Guardar en la lista de notasFinales
    indice = nombres.index(nombreAlumno)
    notasFinales[indice][1] = promedio_general

    # Actualizar el mejor promedio general
    if promedio_general > mejor_promedio:
        mejor_promedio = promedio_general
        mejor_alumno = nombreAlumno

# Mostrar matriz completa de materias con todas las notas
print("\nMatriz completa de materias con notas:")
for fila in materias:
    print(fila)

# Mostrar lista de notas finales con promedios generales
print("\nPromedios generales de todos los alumnos:")
for alumno in notasFinales:
    print(f"{alumno[0]}: {alumno[1]:.2f}")

# Mostrar el alumno con mejor promedio
print(f"\nEl alumno con mejor promedio es {mejor_alumno} con {mejor_promedio:.2f}")
