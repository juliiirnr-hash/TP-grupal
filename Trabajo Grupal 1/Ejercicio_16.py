


arr1 = ["hola",42,"adios"]
arr2 = ["caca","culo","pedo"]



def contieneNumeros(lista):

    contiene = False

    for i in lista:
        if (isinstance(i,(int,float))):
            contiene = True
            break

    if(contiene):
        print("[El array contiene numeros!]")
    else:
        print("[El array no contiene numeros]")




contieneNumeros(arr1)
contieneNumeros(arr2)
