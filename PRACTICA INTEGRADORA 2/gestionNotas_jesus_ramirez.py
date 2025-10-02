          # Legajo: Nombre del alumno.
alumnos = {"60902": "Rodolfo Fernandez",
           "61654": "Luis Gomez",
           "61852": "Andrea Pereira",
           "61754": "Juan Cruz Gonzales"}
           # Materia, nota 1, nota 2, promedio.
materias = [["Ciencias", None, None, None],
            ["Historia", None, None, None],
            ["Geografía", None, None, None],
            ["Matemáticas", None, None, None],
            ["Física", None, None, None]]
            # Nombre, nota final.
notasFinales  = [["Rodolfo Fernandez", None],
                 ["Luis Gomez", None],
                 ["Andrea Pereira", None],
                 ["Juan Cruz Gonzales", None]]

def tomarNotas(alumnos, materias, i):
    while True:
        materias[i][1] = float(input(f"{materias[i][0]}: ¿Cuál es la primera nota del alumno? "))
        if materias[i][1] < 0 or materias[i][1] > 10:
            print("El valor es inválido; debe ser un número del 0 al 10.")
            print()
            continue
        break

    while True:
        materias[i][2] = float(input(f"{materias[i][0]}: ¿Cuál es la segunda nota del alumno? "))
        if materias[i][2] < 0 or materias[i][2] > 10:
            print("El valor es inválido; debe ser un número del 0 al 10.\nIntente de nuevo.")
            print()
            continue
        break

    materias[i][3] = (materias[i][1]+materias[i][2])/2
    print()

def mostrarNotas(materias):
    for i in range(4):
        print(materias[i])

def mostrarMejorMateria(materias):
    nota = -1
    mejorMateria = "n/a"
    for i in range(4):
        if materias[i][3] == nota:
            mejorMateria += ", " + materias[i][0]

        if materias[i][3] > nota:
            nota = materias[i][3]
            mejorMateria = materias[i][0]
    return mejorMateria

iteracion = 0
for key in alumnos:
    print(f"Alumno: {alumnos[key]}.")
    for i in range(4):
        tomarNotas(alumnos, materias, i)

    notasFinales[iteracion][1] = (materias[0][3]+materias[1][3]+materias[2][3]+materias[3][3])/4

    print(f"Notas calificadas de {alumnos[key]}.\nMateria, 1ra nota, 2da nota, promedio.")
    mostrarNotas(materias)
    print(f"Mejor(es) materia(z): {mostrarMejorMateria(materias)}.\nY la nota final es: {notasFinales[iteracion][1]}.")
    print()
    iteracion += 1

for i in range(4):
    nota = -1.0
    mejorNota = ""
    print(notasFinales[i])
    for i in range(4):
        if notasFinales[i][1] == nota:
            mejorNota += ", " + notasFinales[i][0]
        if notasFinales[i][1] > nota:
            nota = notasFinales[i][1]
            mejorNota = notasFinales[i][0]

print(f"Mejor(es) nota(s): {mejorNota}, con {nota} puntos.")
