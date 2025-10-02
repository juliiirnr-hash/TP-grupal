def notamaxima(nota_alta,materias):
    # Calcula la nota más alta del alumno
   notamayor=max(nota_alta)
    # Recorre cada materia para encontrar cuál tiene esa nota
   for nota1 in materias:
        if nota1[3]==notamayor: 
           print(f"La nota {nota1[3]} de la materia {nota1[0]} es la nota mas alta del alumno")
        
def prom_general(nota_alta):
  # Calcula el promedio general del alumno sumando los promedios por materia
   promedio_general=sum(nota_alta)/len(nota_alta)
   return promedio_general

def agregar_promedio(promedio1,notasFinales,posicion):
    # Agrega el promedio general del alumno en su fila correspondiente dentro de notasFinales
   notasFinales[posicion].append(promedio1)
   

def maximo_promedio(notasFinales):
   # Crea una lista con todos los promedios generales
   lista_notas=[]
   for notasf in notasFinales:
      lista_notas.append(notasf[1])

   promedio_mayor=max(lista_notas)  
   for notasf in notasFinales:
      if notasf[1]==promedio_mayor:
         print(f"El alumno con la mayor nota es: {notasf[0]} con {notasf[1]}")
         
      
      
#-------------------------------------Programa Principal----------------------------------------------   
# Diccionario que relaciona legajo con nombre del alumno
alumno={60902:"Rodolfo Fernandez",61654:"Luis Gomez",61852:"Andrea Pereira",61754:"Juan Cruz Gonzales"}
# Lista base con los nombres de las materias
materias=[["Ciencias"],["Historia"],["Geografia"],["Matematicas"],["Fisica"]]
# Lista que guarda el nombre del alumno y su promedio general
notasFinales=[["Rodolfo Fernandez"],["Luis Gomez"],["Andrea Pereira"],["Juan Cruz Gonzales"]]
c=0 # contador para saber en qué posición está cada alumno en notasFinales

for value in alumno.values():
   print(f"Alumno: {value}")
   nota_alta=[]

   for fila in materias:
      print(f"Materia: {fila[0]}")
      i=0
      suma=0
      while i<2:
        nota=float(input(f"Ingrese la nota:{i+1}: "))
        if 0<=nota<=10:
           fila.append(nota)
           i+=1
           suma+=nota
        else:
           print("Debe ingresar una nota mayor a 0")
           continue
      notafinal=suma/2 
      print(f"Nota Final: {notafinal} ")
      fila.append(notafinal)
      nota_alta.append(notafinal)
      
      
   promedio1=prom_general(nota_alta)
   print(f" Materias con notas: \n{materias}")
   notamaxima(nota_alta,materias)
   
   agregar_promedio(promedio1,notasFinales,c)
   c+=1
   materias=[["Ciencias"],["Historia"],["Geografia"],["Matematicas"],["Fisica"]]

print(f"Notas Finales: \n{notasFinales}")
maximo_promedio(notasFinales)

   
    



   

         



 
      
          
           

   
   
      
    




         

      