dato = int(input("ingrese un numero del uno al diez\n"))

def largo(numero):
    if numero <= 3 :
        print("el numero es corto")
    elif numero <= 7 :
        print("el numero es medio")
    elif numero > 7 and numero <= 10:
        print("el numero es largo")
    else:
        print("ingresa valor incorrecto")
        
largo(dato)

# si utilizamos el return podemos hacer lo siguiente

dato = int(input("ingrese un numero del 1 al 10\n"))

def largo_1(numero):
    if numero <= 3 :
        return "el numero es corto"
    elif numero <= 7 :
        return "el numero es medio"
    elif numero > 7 and numero <= 10 :
        return "el numero es largo"
    else:
        return "valor incorrecto"
print(dato,largo_1(dato))
