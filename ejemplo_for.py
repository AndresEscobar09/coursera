# conteo simple
x=12 
for i in range(x):
    print(i)



# for simple
for i in [5,4,3,2,1] :
    print(i)
print("blastoff!")


#recorrer una lista

friends =["Joseph", "Glen", "sally"]
for friend in friends :
    print("happy new year:",friend)
print("done")

# bucle para numero mayor

numero_mayor = -1
print('ahora el numero mayor es:',numero_mayor)
for numero_actual in [9,41,12,3,74,15]:
    if numero_actual > numero_mayor :
        numero_mayor = numero_actual
    print(numero_mayor,numero_actual)
print('por ultimo el numero mayor es :', numero_mayor)

#bucle de numero menor

numero_menor = 100
print('ahora el numero menor es:',numero_menor)
for numero_actual in [9,41,12,3,74,15]:
    if numero_actual < numero_menor :
        numero_menor = numero_actual
    print(numero_menor,numero_actual)
print('por ultimo el numero menor es :', numero_menor)

# bucle menor sin valor de referencia

smallest = None
print("before")
for value in [9,41,12,3,74,15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("after", smallest)
