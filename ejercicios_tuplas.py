#asignacion de una tupla
x = ('Glenn', 'Sally','Joseph')
print(x[2])
y = (1,9,2)
print(y)
print(max(y ))

#se pueden asignar tuplas

(m,n) = (4,'fred')
print(n)
(a,b) = (99,98)
print(a)


#se puede ordenar una dicionario por tuplas

d = {'a':10,'b':1,'c':22}
print(d.items()) 
print(sorted(d.items()))


#obtener tuplas de los dicionarios y almacenarlos en una lista
c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))# se invierte el orden de la tupla
print(tmp)

#ordenar la lista de tuplas de mayor a menor

tmp = sorted(tmp, reverse=True)
print(tmp)

# encontrar el top 10 de palabras usadas en el texto
l = input('ingrese nombre del archivo\n')
fhand = open(l)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] =counts.get(word,0) + 1 
lst = list()
for key,val in counts.items(): 
    newtup = (val,key) # invierte los valores de las tuplas
    lst.append(newtup)
lst = sorted(lst, reverse=True) #ordena de mayor a menor

for val,key in lst[:10]:
    print(key,val)
    
##para ordenar tuplas tambien podemos usar

print(sorted([(v,k) for v,k in c.items()]))
print(sorted([(v,k) for v,k in c.items()]))