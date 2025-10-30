# Función principal del menú q
def menu(paises):
    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("a. Buscar Pais")
        print("b. Filtrar paises")
        print("c. Ordenar paises")
        print("d. Estadisticas del Pais")
        print("e. Salir")

        opcion = input("Ingrese la opción que desea: ").lower()
        if opcion == "a":
            buscar_pais(paises)
            
        elif opcion=="b":
            print("1. Buscar por continente")
            print("2. Rango de Poblacional ")
            print("3.Rango de Superficie")
            opcion1=input("Ingrese la opcion que desea: ")
            if opcion1=="1":
                filtrar_continente(paises)
            elif opcion1=="2":
                rango_poblacion(paises)
            elif opcion1=="3":
                rango_superficie(paises)
            else:
                print("Opcion invalida")
            

          
        elif opcion=="c":
            ordenar_paises(paises)
            ordenar_Poblacion(paises)
        elif opcion=="d":
    
            may_minPoblacion(paises)
            print("-"*30)
            print(f"Promedio de Poblacion Mundial: {prom_poblacion(paises)}")
            print("-"*30)
            print(f"Promedio de la superficie: {prom_superficie(paises)}")
            print("-"*30)
            cant_paisesxCont(paises)
        elif opcion=="e":
            print("Fin del Programa")
            break
        else:
            print("Opción inválida. Intente nuevamente.")  
def lista_paises(paises):
    with open("paises.csv","r") as archivo:
        for linea in archivo:
            diccionario={}
            datos=linea.strip().split(",")
            diccionario["Nombre del Pais"]=datos[0]
            diccionario["Poblacion"]=datos[1]
            diccionario["Superficie"]=datos[2]
            diccionario["Continente"]=datos[3]
            paises.append(diccionario)
    return paises   

def buscar_pais(paises):
    buscarpais=input("Ingresar el pais que deseas buscar: ").capitalize()
    encontrado=False
    for pais in paises:
        if pais["Nombre del Pais"]==buscarpais:
            print(f"{pais["Nombre del Pais"]}\n Poblcion: {pais["Poblacion"]}\n Superficie: {pais["Superficie"]}\n Continente: {pais["Continente"]} ")
            encontrado=True
    if not encontrado:
        print("El Pais ingresado no se encuentra")

def filtrar_continente(paises):
    buscarcontinente=input("Ingresar el continente: ").capitalize()
    encontrado1=False
    print("Paises del Continente ingresado")
    for pais in paises:
        if pais["Continente"]==buscarcontinente:
            print(f"{pais["Nombre del Pais"]}\n  ")
            encontrado1=True
    if not encontrado1:
        print("El Continente ingresado no se encuentra")
def rango_poblacion(paises):
    Muy_Baja_Poblacion=[]
    Poblacion_baja=[]
    Poblacion_Media=[]
    Poblacion_Alta=[]
    Poblacion_MuyAlta=[]
    for pais in paises:
        if int(pais["Poblacion"])<1000000:
            Muy_Baja_Poblacion.append(pais["Nombre del Pais"])
        elif 1000000<=int(pais["Poblacion"])<10000000:
            Poblacion_baja.append(pais["Nombre del Pais"])
        elif 10000000<=int(pais["Poblacion"])<50000000:
            Poblacion_Media.append(pais["Nombre del Pais"])
        elif 50000000<=int(pais["Poblacion"])<100000000:
            Poblacion_Alta.append(pais["Nombre del Pais"])
        else:
            Poblacion_MuyAlta.append(pais["Nombre del Pais"])
    print(f"Paises con cantidad de poblacion Muy Alta:{', '.join(Poblacion_MuyAlta)}")
    print(f"Paises con cantidad de poblacion Alta:{', '.join(Poblacion_Alta)}")
    print(f"Paises con cantidad de poblacion Media:{', '.join(Poblacion_Media)}")
    print(f"Paises con cantidad de poblacion Baja:{', '.join(Poblacion_baja)}")
    print(f"Paises con cantidad de poblacion Muy Baja:{', '.join(Muy_Baja_Poblacion)}")
def rango_superficie(paises):
    Superficie_MuyPequeña=[]
    Superficie_baja=[]
    Superficie_Media=[]
    Superficie_Alta=[]
    Superficie_MuyAlta=[]
    for pais in paises:
        if int(pais["Superficie"])<10000:
            Superficie_MuyPequeña.append(pais["Nombre del Pais"])
        elif 10000<=int(pais["Superficie"])<100000:
            Superficie_baja.append(pais["Nombre del Pais"])
        elif 100000<=int(pais["Superficie"])<1000000:
            Superficie_Media.append(pais["Nombre del Pais"])
        elif 1000000<=int(pais["Superficie"])<3000000:
            Superficie_Alta.append(pais["Nombre del Pais"])
        else:
            Superficie_MuyAlta.append(pais["Nombre del Pais"])
    print(f"Paises con cantidad de Superficie Muy Alta:{', '.join(Superficie_MuyAlta)}")
    print(f"Paises con cantidad de Superficie Alta:{', '.join(Superficie_Alta)}")
    print(f"Paises con cantidad de Superficie Media:{', '.join(Superficie_Media)}")
    print(f"Paises con cantidad de Superficie Baja:{', '.join(Superficie_baja)}")
    print(f"Paises con cantidad de Superficie Muy Baja:{', '.join(Superficie_MuyPequeña)}")

def ordenar_paises(paises):
   paises.sort(key=lambda x: x["Nombre del Pais"])
   print(f"Paises ordenados alfabeticamente:{paises}")
def ordenar_Poblacion(paises):
    paises.sort(key=lambda x: int(x["Poblacion"]))
    print(f"Paises ordenados por Poblacion (ascendente):{paises}")
def ordenar_superficie(paises):
    paises.sort(key=lambda x: int(x["Superficie"]))
    print(f"Paises ordenados por Superficie (ascendente):{paises}")

def may_minPoblacion(paises):
    mayor = max(paises, key=lambda x: int(x["Poblacion"]))
    menor = min(paises, key=lambda x: int(x["Poblacion"]))
    print(f"Pais con mayor poblacion: {mayor["Nombre del Pais"]} con {mayor["Poblacion"]} habitantes")  
    print(f"Pais con manor poblacion: {menor["Nombre del Pais"]} con {menor["Superficie"]} habitantes")    
  
def prom_poblacion(paises):
    suma=0
    for pais in paises:
        suma+=int(pais["Poblacion"])
    return suma/(len(paises))
def prom_superficie(paises):
    suma1=0
    for pais in paises:
        suma1+=int(pais["Superficie"])
    return suma1/(len(paises))
def cant_paisesxCont(paises):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    for pais in paises:
        if pais["Continente"]=="Europa":
            a+=1
        if pais["Continente"]=="America":
            b+=1
        if pais["Continente"]=="Africa":
            c+=1
        if pais["Continente"]=="Asia":
            d+=1
        if pais["Continente"]=="Oceania":
            e+=1
        if pais["Continente"]=="Antartida":
            f+=1
    print("Cantidad de paises por continente")
    print(f"America: {b}\n Europa: {a}\n Africa: {c} \n Asia: {d}\n Oceania: {e} \n Antarntida: {f}")

paises=[]
paises=lista_paises(paises)
print(paises)
menu(paises)

        
