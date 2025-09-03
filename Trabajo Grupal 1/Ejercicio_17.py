
# [ EJERCICIO 17 ]:

class FuncionesPrograma:

    meses_texto = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

    @staticmethod
    def getFechaString(fecha: str) -> str:

        dia, mes, anio = fecha.split("/")
        
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        dias_texto = {
            1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco",
            6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
            11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce",
            15: "Quince", 16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho",
            19: "Diecinueve", 20: "Veinte", 21: "Veintiuno", 22: "Veintidós",
            23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco",
            26: "Veintiséis", 27: "Veintisiete", 28: "Veintiocho",
            29: "Veintinueve", 30: "Treinta", 31: "Treinta y uno"
        }

        if anio == 1900:
            anio_texto = "mil novecientos"
        elif anio == 2000:
            anio_texto = "dos mil"
        else:
            anio_texto = str(anio)  # no voy a hacer todas las combinaciones profe

        return f"{dias_texto[dia]} de {FuncionesPrograma.meses_texto[mes]} de {anio_texto}"


class Principal:
    def main():
        fecha = "21/08/2000"
        resultado = FuncionesPrograma.getFechaString(fecha)
        print(resultado)



Principal.main()
