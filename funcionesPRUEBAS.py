from pprint import pprint

#Ejercicio---1

def num_par():
    try:
        num1= int(input("Ingrese un valor: "))
        if num1 %2==0:
            print("El numero ingresado es par")
        else:
            print("El numero ingresado es impar")
    except:
        print("ERROR! Ingrese solo numeros")
        num_par()
num_par()

#Ejercicio---2

dato=input("Ingrese su correo electronico: ")
def es_correo(dato):
    correo=dato
    if "@" and ".com" and " " in correo:
        print("El correo es valido")
    else:
        print("El correo es invalido")
es_correo(dato)

#Ejercicio---3

def numdni():
    try:
     num1=int(input("Ingrese su numero de DNI: "))
     if num1>999999 and num1<100000000:
         print("El numero de DNI es valido")
     else:
         print("El numero de DNI es invalido")
    except:
        print("ERROR! Ingrese solo numeros")
        numdni()
numdni()