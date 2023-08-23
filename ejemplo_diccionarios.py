#declarar y asignar elementos en un diccionario
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)

print(purse['candy'])

purse['candy'] = purse['candy']+2
print(purse)


jjj = {'chuck' : 1, 'fred' : 42, "jan" : 100}

print(jjj)

ooo = {} #se puede crear un dicionario vacio
print(ooo)

# contar cadenas repetidas de una lista usando un diccionario.
  

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

#una forma mas sencilla de hacerlo es:

if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name,0)
print(counts)

# contar palabras repetidas en un texto que se ingrese

palabras = dict()
line = input('Enter a line of text:\n')
words = line.split() # se utiliza para pasar el string a una lista
print('Words:',words)

print('counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('counts', counts)

#recorrer un diccionario
for key in counts:
    print(key,counts[key])
#listas de claves o lostas de llaves

print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#recorrer un dicionario utilizando metodos
for aaa,bbb in jjj.items() :
    print(aaa,bbb)
