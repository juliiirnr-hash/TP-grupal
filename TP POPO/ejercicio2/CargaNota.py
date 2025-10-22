from Alumno import Alumno
from Nota import Nota

class CargaNota:
    def main():
        alumnos = []

        while True:
            nombreAlumno = input("Ingrese el nombre completo del alumno/a (x para salir): ")
            if nombreAlumno.lower() == "x":
                break

            legajo = int(input("Ingrese el legajo del alumno/a: "))

            notas = []
            while True:
                catedra = input("Ingrese la cátedra (x para salir): ")
                if catedra.lower() == "x":
                    if len(notas) == 0:
                        print("Debe ingresar al menos una nota.")
                        continue
                    break

                notaExamen = float(input("Ingrese la nota del examen: "))
                nota = Nota(catedra, notaExamen)
                notas.append(nota)

            alumno = Alumno(nombreAlumno, legajo, notas)
            alumnos.append(alumno)

        print("\nINFORME ALUMNOS\n-------------------------------------------------")
        for alumno in alumnos:
            print(f"\n{alumno.nombreCompleto} (Legajo: {alumno.legajo})")
            for n in alumno.notas:
                print(f"  Cátedra: {n.catedra} - Nota: {n.notaExamen}")
            print(f"Promedio: {alumno.promedio():.2f}")


if __name__ == "__main__":
    CargaNota.main()
