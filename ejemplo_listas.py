#concatenar cadenas
a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print(c)

#seleccionar elementos dentro de una lista

print(c[1:6])


# agregar elemtos a una lista.
stuff = list()
stuff.append('book')#comentario 
stuff.append(99)
stuff.append('cookie')
print(stuff)

#saber si un elemento esta en la lista (salida booleana)

1 in a

# odenar lista por orden alfabetico

names =['Ana','Mary','Andres','Carlos']
print(names)
names.sort()
print(names)

# funciones para numeros de una lista

print(c)
print(len(c)) #cuabtos elementos tiene la lista
print(max(c))# elemento mayor 
print(min(c)) #elemento menor
print(sum(c)) #sumar los elemetos
print(sum(c)/len(c)) #promedio de los elementos

#calular el promedio de los numeros ingresados

numberlist= list()
while True:

    add = input('enter a number:\n')
    if add == 'done':
        break
    value = float(add)
    numberlist.append(value)
average = sum(numberlist)/len(numberlist)
print('average:',average)

#convertir un string en una lista

abc = 'with there words'
print(abc)
stuff = abc.split()
print(stuff)
print(stuff[0])

#recorrer una lista

for w in stuff:
    print(w)

#separar palabras por ;

line = 'first-second-third'
print(line)
thing = line.split('-')
print(thing)

#analizar datos planos convirtiendolos en listas

#extraer los dias en los que se reciben los correos

fhand =open('archivos_planos\mbox-short.txt')

for line in fhand:
    line = line.rstrip()  #convierta el renglon en un string
    if not line.startswith('From '): # si el renglon no contiene la palabra front: continue al siguiente
        continue
    words = line.split() # pasar el string a un lista
    print(words[2])#imprimir la posicion 2 de la lista
    
    







    
