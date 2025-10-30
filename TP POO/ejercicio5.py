


# - [ Ejercicio 5 ] -


class Barrio(): # --------------------------------------------------------------------- [Barrio]


    def __init__(self,nombre:str,empresaConstructora:str,viviendas:list):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = viviendas

    def getSuperficieTotalTerreno(self):
        total = 0
        for viv in self.viviendas:
            total += viv.superficieTerreno
        return total
    
    
    def getSuperficieTotalTerrenoXManzana(self, manzana):
        total = 0
        for viv in self.viviendas:
            if (viv.manzana == manzana):
                total += viv.superficieTerreno
        return total

    def getSuperficieTotalCubierta(self):
        total = 0
        for viv in self.viviendas:
            total += viv.getMetrosCuadradosCubiertos()
        return total




class Vivienda():# --------------------------------------------------------------------- [Vivienda]

    def __init__(self,calle:str,numero:int,manzana:str,nroCasa:int,superficieTerreno:float,habitaciones:list):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = habitaciones

    def getMetrosCuadradosCubiertos(self):
        try: 
            totalMetros = 0
            for hab in self.habitaciones:
                totalMetros += hab.metrosCuadrados
                if (totalMetros > self.superficieTerreno):
                    raise ValueError("[!] La superficie cubierta no puede ser mayor a la superficie del terreno” ") 
            return totalMetros
        except ValueError as err:
            print(err)
            return None



class Habitacion(): # --------------------------------------------------------------------- [Habitacion]

    def __init__(self,nombre:str,metrosCuadrados:float):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados






h1 = Habitacion("Dormitorio", 12.0)
h2 = Habitacion("Living", 20.0)
h3 = Habitacion("Cocina", 10.0)
h4 = Habitacion("Comedor", 25.0)
h5 = Habitacion("Baño", 6.5)


v1 = Vivienda("San Martín", 123, "A", 1, 200.0, [h1, h2, h5])
v2 = Vivienda("Belgrano", 45, "A", 2, 150.0, [h3, h5])         
v3 = Vivienda("Sarmiento", 89, "B", 3, 180.0, [h1, h4])

viviendas = [v1, v2, v3]

b = Barrio("Barrio Centro", "Constructora XYZ", viviendas)

print("=== PRUEBAS DE MÉTODOS ===")

print("a) Superficie total de terreno del barrio:",b.getSuperficieTotalTerreno(), "m²")

print("b) Superficie total de terreno en manzana 'A':",b.getSuperficieTotalTerrenoXManzana("A"), "m²")

 
print("c) Metros cuadrados cubiertos por vivienda:")
for v in viviendas:
    try:
        mc = v.getMetrosCuadradosCubiertos()
        print(f"   - Vivienda manzana {v.manzana}, casa {v.nroCasa}: {mc} m²")
    except Exception as e:
        print(f"   - Vivienda manzana {v.manzana}, casa {v.nroCasa}: ERROR -> {e}")

print("d) Superficie total cubierta del barrio:", b.getSuperficieTotalCubierta(), "m²")