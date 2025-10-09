# Función principal del menú que se repite hasta que el usuario decida apagar la máquina
def menu():
    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("a. Agregar Alumno")
        print("b. Ver Alumnos")
        print("c. Generar y mostrar archivo de aprobados")
        print("d. Salir")

        opcion = input("Ingrese la opción que desea: ").lower()
        if opcion == "a":
            agregar_alumno(alumnos,nombreyapellido,alumno1,c)
        elif opcion=="b":
            leer_alumnos()
        elif opcion=="c":
            guardar_aprobados()
        elif opcion=="d":
            print("Fin del Programa")
            break
        else:
            print("Opción inválida. Intente nuevamente.")          
  
#Funcion para agregar alumnos

def agregar_alumno(alumnos,nombreyapellido,alumno1,c):
    nombreyapellido=[]
    alumno1={}
    while True:
        nombre = input("Ingresa el nombre del alumno: ").strip().title()
        if nombre == "":
            print("No ingresaste nada. Intentá de nuevo.")
        elif any(char.isdigit() for char in nombre):
            print(" El nombre no puede contener números.")
        elif not nombre.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras y espacios.")
        else:
            break
   
    nombreyapellido.append(nombre)
    while True:
        apellido = input("Ingresa el apellido del alumno: ").strip().title()
        if apellido=="":
            print("No ingresaste nada. Intentá de nuevo.")
        elif any(char.isdigit() for char in apellido):
            print(" El apellito no puede contener números.")
        elif not apellido.replace(" ", "").isalpha():
            print("El apellido solo puede contener letras y espacios.")
        else:
            break
    nombreyapellido.append(apellido)

    while True:
        legajo =input("Ingresá Legajo: ").strip()
        if legajo == "":
            print(" No ingresaste nada.")
        elif not legajo.isdigit() or len(legajo)!=5:
            print("Se permiten números enteros y con 5 digitos.")
        else:
            legajo1=int(legajo)
            if legajo1> 0:
                break
            else:
                print(" El número debe ser mayor que cero.")  
                continue
    
    while True:
        promedio=input("Ingresá el promedio: ")
        if promedio == "":
            print("❌ No ingresaste nada.")
            continue
        try:
            promedio1 = float(promedio)
            if promedio1 > 0:
                print(" Promedio válido:", promedio)
                break
            else:
                print(" El promedio debe ser mayor que cero.")
        except ValueError:
             print(" Debe contener solo números.")
    
    
    if c==0:
        alumnos[legajo1]=nombreyapellido
        with open("C:/Users/Cara Palida/Downloads/alumnos.txt", "w") as archivo:
            # Escribe los datos en una sola línea, separados por comas
            archivo.write(f"{nombre},{apellido},{legajo1},{promedio1}\n")
            c+=1
    else:
        if validar_existe_alumno(legajo1,alumnos)==False:
            alumnos[legajo1]=nombreyapellido
            with open("C:/Users/Cara Palida/Downloads/alumnos.txt", "a") as archivo:
                archivo.write(f"{nombre},{apellido},{legajo1},{promedio1}\n")
        else:
            print(f"El legajo {legajo1} ya existe en el archivo alumnos.txt, no sepermite su escritura.")
    print(alumnos)    
    while True:
        opcion1 = input("¿Querés registrar otro alumno (si) o volver al menú (M)? ").strip().lower()
        if opcion1 == "si":
            agregar_alumno(alumnos,nombreyapellido,alumno1,c)
            break
        elif opcion1 == "m":
            print("Volviendo al menú...")
            break
        else:
            print("Opción inválida.")

    
#Funcion para validar si existe el alumno  

def validar_existe_alumno(buscado,alumnos):
    encontrado=False
    if buscado in alumnos:
        encontrado=True
    return encontrado
#Mostrar los alumnos con sus datos
def leer_alumnos():
    with open("C:/Users/Cara Palida/Downloads/alumnos.txt","r") as archivo_entrada, \
         open("C:/Users/Cara Palida/Downloads/aprobados.txt", "w") as archivo_salida:
        for linea in archivo_entrada:
            datos=linea.strip().split(",")
            print(f"Nombre y Apellido: {datos[0]} {datos[1]}, Legajo: {datos[2]}, Promedio: {datos[3]}")
#Funcion para guardar los aprobados
def guardar_aprobados():
    d=0
      
    with open("C:/Users/Cara Palida/Downloads/alumnos.txt","r") as archivo:
         
        for linea in archivo:
            datos = linea.strip().split(",")
            nota = float(datos[3])
            if nota >= 6:
                if d==0:
                    with open("C:/Users/Cara Palida/Downloads/aprobados.txt", "w") as archivo:
                        archivo.write(f"{datos[0]},{datos[1]},{nota}\n")
                        d=+1
                else:  
                     with open("C:/Users/Cara Palida/Downloads/aprobados.txt", "a") as archivo:
                        archivo.write(f"{datos[0]},{datos[1]},{nota}\n")
    print("Alumnos Aprobados\n")
    with open("C:/Users/Cara Palida/Downloads/aprobados.txt","r") as archivo:
        for linea in archivo:
            datos1=linea.strip().split(",")
            print(f"Nombre y Apellido: {datos1[0]} {datos1[1]}, Promedio: {datos1[2]}")        


                

               
#-------------PROGRAMA PRINCIPAL           


alumnos={}
alumno1={}
nombreyapellido=[]
c=0
menu()
