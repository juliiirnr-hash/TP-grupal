class Alumno:
    def __init__(self, nombreCompleto, legajo, notas):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        total = sum(n.notaExamen for n in self.notas)
        return total / len(self.notas)




