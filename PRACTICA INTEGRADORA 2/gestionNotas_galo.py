
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

materias = [
    ["Ciencias", "", "", ""],
    ["Historia", "", "", ""],
    ["Geografia", "", "", ""],
    ["Matematicas", "", "", ""],
    ["Fisica", "", "", ""   ]
]

notasFinales = [
    ["Rodolfo Fernandez", ""],
    ["Luis Gomez", ""],
    ["Andrea Pereira", ""],
    ["Juan Cruz Gonzales", ""]
]

def promedioNotas(a,b):
    return (a+b)/2

def obtenerPromedioFinal():
    total = 0
    for mat in materias:
        total += mat[3]
    return total / len(materias)

def mostrarNotas():
    for mate in materias:
        print(mate)

contadorAlumno = -1
for alum in alumnos:
    contadorAlumno += 1

    print("")
    print(f"Notas de {alumnos[alum]}")

    for mate in materias:
        while True:
            nota1 = int(input(f"[Ingrese la primera nota de {mate[0]}]:"))
            if (nota1 > 0 and nota1 < 11):
                break
            else:
                print("[!] La nota debe estár entre 1 y 10")

        while True:
            nota2 = int(input(f"[Ingrese la segunda nota de {mate[0]}]:"))
            if (nota2 > 0 and nota2 < 11):
                break
            else:
                print("[!] La nota debe estár entre 1 y 10")

        promedio = promedioNotas(nota1,nota2)
        mate[1] = nota1
        mate[2] = nota2
        mate[3] = promedio
    
    promedioFinal = obtenerPromedioFinal()

    print("")
    print(f"-- Notas de {alumnos[alum]} --")
    mostrarNotas()
    print(f"-- Promediio final: {promedioFinal} --")
    notasFinales[contadorAlumno][1] = promedioFinal

print("")
print(notasFinales)

print("")
print("//// FIN PROGRAMA ////")
