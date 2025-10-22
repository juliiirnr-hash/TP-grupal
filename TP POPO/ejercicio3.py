class Ingrediente: #Clase que representa un ingrediente con nombre, cantidad y unidad de medida
    def __init__(self,nombre,cantidad,unidad_de_medida):
        self.nombre=nombre 
        self.cantidad=cantidad
        self.unidad_de_medida=unidad_de_medida
    def __str__(self):     #Representación en texto del ingrediente
        return f"{self.nombre} {self.cantidad} {self.unidad_de_medida} "
    
class Plato:
    def __init__(self,nombreCompleto,precio,esBebida): ## Clase que representa un plato o bebida del menú
        self.nombreCompleto=nombreCompleto
        self.precio=precio
        self.esBebida=esBebida
        self.lista_de_ingredientes=[] # Lista para almacenar ingredientes si es comida
    def agregar_ingredientes(self,ingrediente ):
        #Agregar el ingrediente ingresado a la lista de ingredientes
        self.lista_de_ingredientes.append(ingrediente)
    def buscar_valor (self,ingrediente):
        # Verifica si ya existe en la lista de ingredientes
       for buscado in self.lista_de_ingredientes:
          if buscado.nombre==ingrediente.nombre:
              return True
       return False
    
# Clase principal que gestiona el menú del restaurante
class MenuRestaurant:
    def main(self):
        platos = [] #Lista de Plato y Bebidas
       
        while True:
            print("Ingresar plato o bebidad para el Menu. Elija la opcion deseada:  ")
            opcion=input("Comida(a)\n Bebida (otra letra)  \n").lower()
            #Segun la opcion elegida por el usuario, se le asignara el valor de verdad del atributo
            if opcion!="a":
                esBebida=True 
            else:
                esBebida=False

            while True:
                nombreCompleto= input("Ingresa el nombre completo del Plato o Bebida: ").strip().title()
                #Validacion del nombre del plato
                if nombreCompleto== "":
                    print("No ingresaste nada. Intentá de nuevo.")
                    continue
                nombre_existente = any(al.nombreCompleto == nombreCompleto for al in platos)
                if nombre_existente :
                    print("El nombre ya existe.")
                    continue
                else:
                    break
                
            while True:
                        valor1=input("Ingresá el precio: ")
                        if valor1 == "":
                            print("No ingresaste nada.")
                            continue
                        try:
                            precio = float(valor1)
                            if precio > 0:
                            
                                break
                            else:
                                print(" El precio debe ser mayor que cero.")
                        except ValueError:
                            print(" Debe contener solo números.")
            # Crea el objeto Plato
            plato=Plato(nombreCompleto,precio,esBebida)
           #Si es verdadero ingresa a pedirle los ingredientes al usuario
            if esBebida==False:
                print("INGREDIENTES DEL PLATO")
                while True:
                    while True:
                        nombre= input("Ingresa el nombre del ingrediente: ").strip().title()
                        if nombre== "":
                            print("No ingresaste nada. Intentá de nuevo.")
                            continue
                        else:
                            break
                    while True:
                        valor=input("Ingresá la cantidad: ")
                        if valor == "":
                            print("No ingresaste nada.")
                            continue
                        try:
                            cantidad = float(valor)
                            if cantidad > 0:
                            
                                break
                            else:
                                print(" La cantidad debe ser mayor que cero.")
                        except ValueError:
                            print(" Debe contener solo números.")
                    while True:
                        unidad_de_medida= input("Ingresa la unidad de medidad (gramos,unidad, litros o kg): ").strip().title()
                        if unidad_de_medida== "":
                            print("No ingresaste nada. Intentá de nuevo.")
                            continue
                        else:
                            break
                    # Crea el ingrediente y verifica si ya existe
                    ingrediente=Ingrediente(nombre,cantidad,unidad_de_medida)
                    existe = plato.buscar_valor(ingrediente)
                    if(existe):
                       print("el valor ya existe, ingrese nuevos valores")
                       continue
                    else:
                        plato.agregar_ingredientes(ingrediente)
                    opcion2=input("Desea ingresar otro ingrediente (si o no): ").lower()
                    if opcion2!="si":
             
                       break
            #Se agrega a la lista de platos
            platos.append(plato)
            opcion3=input("Desea ingresar otro producto (si o no): ").lower()
            if opcion3!="si":
                break
        print("-----------------MENU---------------------")
        #Recorremos la lista platos
        for plato in platos:
            print("-"*30)
            print(f"\n {plato.nombreCompleto} \n Tipo:{"Bebida" if plato.esBebida==True else "Comida"}\n Precio: {plato.precio} ")
            if plato.esBebida==False:
                print("Ingredientes")
                for ingrediente in plato.lista_de_ingredientes:
                    print(f"Nombre:{ingrediente.nombre}\nCantidad: {ingrediente.cantidad} {ingrediente.unidad_de_medida}")
            print("-"*30)

 # Ejecuta el programa           
menu=MenuRestaurant()      
menu.main()


                




    

