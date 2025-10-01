
#1: Diccionario de alumnos. Legajo de alumnos - nombres
alumnos = {
    60902 : "Rodolfo Fernandez",
    61654 : "Luis Gomez",
    61852 : "Andrea Pereira",
    61754 : "Juan Cruz Gonzales"
}

#2: Lista de materias de dos dimensiones. Materia - Nota1 - Nota2 - Nota Final
materias = [
    ["Ciencias", 0, 0, 0],
    ["Historia", 0, 0, 0],
    ["Geografia", 0, 0, 0],
    ["Matematicas", 0, 0, 0],
    ["Fisica", 0, 0, 0]

]

#3: Crear una lista con las notas finales. Nombre del alumno - nota 

notasFinales = [
    ["Rodolfo Fernandez", 0],
    ["Luis Gomez", 0],
    ["Andrea Pereira", 0],
    ["Juan Cruz Gonzales", 0]

]


i = 0
for legajo, nombre in alumnos.items():
    print("\n alumno: ", nombre) 
    suma = 0
    mejor_materia = ""
    mejor_nota = -1

    #iterar sobre las materias

    for materia in materias:
        nota1 = -1
        while nota1 < 0 or nota1 > 10:
            nota1 = float(input(f"Por favor ingrese la primera nota de {materia[0]}: "))
        
        nota2 = -1
        while nota2 < 0 or nota2 > 10:
            nota2 = float(input(f"Por favor ingrese la segunda nota de {materia[0]}: "))
       
        notaFinal = (nota1 + nota2) / 2

        materia[1] = nota1
        materia[2] = nota2
        materia[3] = notaFinal

        print(f"Nota Final de {materia[0]} = {materia[3]}")

        suma = suma + notaFinal
        if notaFinal > mejor_nota:
            mejor_nota = notaFinal
            mejor_materia = materia[0]

    print("\n Notas :) :")
    for materia in materias:
        print(materia[0]," Nota 1 = ", materia[1], "Nota 2 =", materia[2], "Nota Final : ", materia[3])

    promedio = suma / len(materias)
    notasFinales[i][1] = promedio
    print(f"Mejor materia: {mejor_materia}")
    print(f"Mejor nota: {mejor_nota}")
    print(f"Promedio: {promedio}")
    i = i + 1


#mejor promedio

mejor = notasFinales[0]
for notasf in notasFinales:
    if notasf[1] > mejor[1]:
        mejor = notasf

print("\n Notas Finales: ", notasFinales)
print("El mejor promedio es de :", mejor[0])



