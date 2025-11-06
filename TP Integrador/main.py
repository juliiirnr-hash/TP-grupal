from Pais import Pais #Importar Clase Pais



# ------------------------------------------ Lectura
def lista_paises():
    listaPaises = []
    with open("paises.csv","r", encoding="iso-8859-1") as archivo:
        for linea in archivo:
            datos=linea.strip().split(",")

            pais = Pais(datos[0],int(datos[1]),datos[3],float(datos[2]))

            listaPaises.append(pais)
    return listaPaises



# ------------------------------------------ Funciones Primarias

def buscar_pais(paises):
    buscarpais = input("Ingresar el pais que deseas buscar: ").lower()
    encontrado = False

    for pais in paises: # Busca pais comparando con pais ingresado hasta encontrarlo
        if buscarpais in pais.nombre.lower():
            print(f"    {pais.nombre}\n Poblacion: {pais.poblacion} habitantes\n Superficie: {pais.superficie} km2\n Continente: {pais.continente} ")
            print()
            encontrado=True
    
    if not encontrado: # En caso de no encontrarlo
        print("El Pais ingresado no se encuentra")



def filtrar_paises():
    while True:
        print("1. Buscar por continente")
        print("2. Rango poblacional")
        print("3. Rango de superficie")
        print("4. Volver atrás")
        opcion1 = input("Ingrese la opción que desea: ")


        match opcion1: # Caso por cada opcion
            case "1":
                filtrar_por_continente(paises)
            case "2":
                rango_poblacion(paises)
            case "3":
                rango_superficie(paises)
            case "4":
                print()
                break
            case _:
                print("[!] Opción inválida") # Caso fallback


def ordenar_paises(paises):
    paises.sort(key=lambda x: x.nombre) # Recorre y ordena alfabeticamente
    print("")
    print("--- Paises ordenados alfabeticamente:")
    for pais in paises:
        print(pais.nombre)

def ordenar_poblacion(paises):
    paises.sort(key=lambda x: x.poblacion) # Recorre y compara la poblacion para ordenar
    print("")
    print("--- Paises ordenados por Poblacion (ascendente):")
    for pais in paises:
        print(pais.nombre)

def ordenar_superficie(paises):
    paises.sort(key=lambda x: x.superficie) # Recorre y compara la superficie para ordenar
    print("")
    print("--- Paises ordenados por Superficie (ascendente):")
    for pais in paises:
        print(pais.nombre)


def filtrar_por_continente(paises):
    continente = input("Ingresar el continente: ").capitalize()
    encontrado1 = False
    print("Paises del Continente ingresado")
    for pais in paises:
        if pais.continente == continente:
            print(f"{pais.nombre}\n  ")
            encontrado1=True
    if not encontrado1:
        print("El Continente ingresado no se encuentra")


def rango_poblacion(paises):
    Poblacion_Baja = []
    Poblacion_Media = []
    Poblacion_Alta = []
    Poblacion_MuyAlta = []

    for pais in paises:
        if pais.poblacion < 20000000:
            Poblacion_Baja.append(pais.nombre)
        elif pais.poblacion < 100000000:
            Poblacion_Media.append(pais.nombre)
        elif pais.poblacion < 500000000:
            Poblacion_Alta.append(pais.nombre)
        else:
            Poblacion_MuyAlta.append(pais.nombre)

    print("")
    print(f"Países con población Baja: {', '.join(Poblacion_Baja)}\n")
    print(f"Países con población Media: {', '.join(Poblacion_Media)}\n")
    print(f"Países con población Alta: {', '.join(Poblacion_Alta)}\n")
    print(f"Países con población Muy Alta: {', '.join(Poblacion_MuyAlta)}\n")
    print("")


def rango_superficie(paises):
    Superficie_Baja = []
    Superficie_Media = []
    Superficie_Alta = []
    Superficie_MuyAlta = []

    for pais in paises:
        superficie = int(pais.superficie)

        if superficie < 500000:  
            Superficie_Baja.append(pais.nombre)
        elif superficie < 2000000:  
            Superficie_Media.append(pais.nombre)
        elif superficie < 5000000:  
            Superficie_Alta.append(pais.nombre)
        else:  
            Superficie_MuyAlta.append(pais.nombre)

    print("")
    print(f"Paises con Superficie Baja: {', '.join(Superficie_Baja)}\n")
    print(f"Paises con Superficie Media: {', '.join(Superficie_Media)}\n")
    print(f"Paises con Superficie Alta: {', '.join(Superficie_Alta)}\n")
    print(f"Paises con Superficie Muy Alta: {', '.join(Superficie_MuyAlta)}\n")
    print("")


def may_minPoblacion(paises):
    mayor = max(paises, key=lambda x: x.poblacion)
    menor = min(paises, key=lambda x: x.poblacion)
    print(f"Pais con mayor poblacion: {mayor.nombre} con {mayor.poblacion} habitantes")
    print("-" * 30)
    print(f"Pais con menor poblacion: {menor.nombre} con {menor.poblacion} habitantes")
   
   

def prom_poblacion(paises):
    suma=0
    for pais in paises:
        suma+=int(pais.poblacion) # Suma la poblacion de cada pais

    return suma/(len(paises)) # Retorna el promedio de la poblacion


def prom_superficie(paises):
    suma1=0
    for pais in paises:
        suma1+=int(pais.superficie) # Suma la superficie de cada pais

    return suma1/(len(paises)) # Retorna el promedio de superficie



def cant_paisesxCont(paises):

    # Variables para conteo por continente
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0

    for pais in paises:
        if pais.continente =="Europa":
            a+=1
        if pais.continente =="America":
            b+=1
        if pais.continente =="Africa":
            c+=1
        if pais.continente =="Asia":
            d+=1
        if pais.continente =="Oceania":
            e+=1
        if pais.continente =="Antartida":
            f+=1

    print("Cantidad de paises por continente:") # Imprimer conteo de cada continente
    print(f" America: {b}\n Europa: {a}\n Africa: {c} \n Asia: {d}\n Oceania: {e} \n Antartida: {f}")






# ----------------------------------------------------- MAIN --


def menu(paises): # Función principal del menú
    print("   AVISO: PARA GARANTIZAR EL FUNCIONAMIENTO CORRECTO PROGRAMA, SE HA DECIDIDO OMITIR\nLAS TILDES Y EÑES DEL ARCHIVO .CSV.")
    print("   Esto significa que España figura en él como 'Espania', y que tanto países como\ncontinentes con tilde ahora figuran con caracteres comunes. Esperamos su comprensión.")

    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("a. Buscar País")
        print("b. Filtrar países")
        print("c. Ordenar países")
        print("d. Estadísticas de países")
        print("e. Salir")

        opcion = input("Ingrese la opción que desea: ").lower()
        print("")


        match opcion:  # Caso por cada opcion
            case "a":
                buscar_pais(paises)
            case "b":
                filtrar_paises()
            case "c":
                ordenar_paises(paises)
                try:
                    input("   Ingrese caulquier valor para continuar. ")
                except Except:
                    print("Ha ocurrido un imprevisto. ")

                ordenar_poblacion(paises)
                try:
                    input("   Ingrese caulquier valor para continuar. ")
                except Except:
                    print("Ha ocurrido un imprevisto. ")

                ordenar_superficie(paises)
            case "d":
                may_minPoblacion(paises)
                print("-" * 30)
                print(f"Promedio de Población Mundial: {round(prom_poblacion(paises),2)} habitantes")
                print("-" * 30)
                print(f"Promedio de la superficie: {round(prom_superficie(paises), 2)} km2")
                print("-" * 30)
                print()
                cant_paisesxCont(paises)
            case "e":
                print("/// Fin del Programa ///")
                break
            case _:
                print("[!] Opción inválida. Intente nuevamente.")


paises = lista_paises()
menu(paises)
