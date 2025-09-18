# Función principal del menú que se repite hasta que el usuario decida apagar la máquina
def menu():
    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("a. Pedir golosinas")
        print("b. Mostrar golosinas")
        print("c. Rellenar golosinas (técnico)")
        print("d. Apagar máquina")

        opcion = input("Ingrese la opción que desea: ").lower()
        if opcion == "a":        # Opción para que un empleado solicite golosinas

            Sol_legajo = input("Ingrese su legajo: ")
            validacion_de_identidad(Sol_legajo, empleados, 0)
        elif opcion == "b":            # Opción para mostrar el stock actual de golosinas
            Mostrar_golosinas(golosinas)
        elif opcion == "c":               # Opción exclusiva para técnicos que permite recargar golosinas
            validacion_tecnico(clavesTecnico)
        elif opcion == "d":            # Opción para apagar la máquina y mostrar lo que se pidió
            print("Apagando máquina...")
            print(f"Golosinas perdidas: {golosinasPedidas}")
            break   
        else:
            print("Opción inválida. Intente nuevamente.")           # Si la opción ingresada no es válida
  
  
# Función que muestra todas las golosinas disponibles con su stock
def Mostrar_golosinas(golosinas):
   for filas in golosinas:
      text =filas[1].ljust(18, ' ')       # Alinea el nombre para que se vea ordenado
      print(f"{text}   | {filas[2]} ")    # Muestra nombre y stock
    
    
# Función que valida si el legajo ingresado pertenece a un empleado
def validacion_de_identidad(sol_legajo,empleados,cantidad):
   for datos in empleados.values():
     if datos["legajo"] == sol_legajo:
        cod_solicitado=int(input("Ingrese el codigo de la golosina: "))
        pedido_golosina(cod_solicitado,golosinas,cantidad,clavesTecnico)
        return    # Sale de la función si el legajo es válido
   else: 
     print("Usted no es un empleado de la empresa" )    # Si no se encuentra el legajo
        
# Función que permite al empleado pedir una golosina si hay stock suficiente
def pedido_golosina(cod_solicitado,golosinas,cantidad,clavesTecnico):
   
   for fila in golosinas[1:]:          # Salta el encabezado
      if fila[0]==cod_solicitado:
        cantidad+=int(input(f"Cuanto/as {fila[1]} quiere?"))
        if 0<cantidad<=fila[2]:             # Verifica si hay stock suficiente
              fila[2]=fila[2]-cantidad
              golosinasPedidas.append([fila[0],fila[1],cantidad])
              print("✅ Golosina agregada al pedido.")
        else:
              print(f"Lo sentimos la golosina {fila[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")


        return            # Sale de la función después de procesar
      
              
    
 # Función que valida la contraseña del técnico y permite recargar golosinas  

def validacion_tecnico(clavesTecnico):
   cantidad=0
   contraseñaCorrecta= "".join(clavesTecnico)
   entrada=input("Ingrese la contraseña: ")
   if entrada == contraseñaCorrecta:
      print(" Ingreso autorizado")
      codigo2=int(input("Ingrese el codigo de golosina que desea recargar: "))
      for fila in golosinas[1:]:
         if fila[0]==codigo2:
           
               cantidad+=int(input(f"Cuanto/as {fila[1]} quiere? "))
               if cantidad>0:
                 fila[2]=cantidad+fila[2]
                 print(golosinas)
                 
               else:
                    print("Ingrese una cantidad mayor a cero")
               return
      print("❌ Código no encontrado.")
   else:
            print("❌ Ingreso no autorizado")
            
        
   
# ---------------------- PROGRAMA PRINCIPAL ----------------------
# Lista de golosinas con su código, nombre y stock inicial
golosinas=[["Codigo","Nombre de golosina", "stock"],
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]
# Lista donde se guardan las golosinas que fueron pedidas
golosinasPedidas= []
# Diccionario de empleados con su nombre y legajo
empleados = {"José Alonso":{"legajo":"1100"},
             "Federico Pacheco":{"legajo":"1200"},
             "Nelson Pereira":{"legajo":"1300"},
             "Osvaldo Tejada":{"legajo":"1400"},
             "Gastón Garcia":{"legajo":"1400"}
}


# Tupla con las claves que forman la contraseña del técnico
clavesTecnico=("admin","CCCDDD","2020")

print("Bienvendidos a nuestro Kiosco personal")
cantidad=0
# Llama al menú principal para iniciar el programa
menu()
