import re


print('my 2 favorite numbers are 19 and 42')

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # crea una lista con los valores numericos que encuentra de 1 o varias cifras.
print('imprime los numeros de uno o mas digitos que se encuetran en la anterior cadena')
print(y)

#ejercicio 2 
print("\nEncontrar e imprimir los caracteres que esten entre 'f' y ':'\n")

x = 'From: Using the: character'
print(x)
y = re.findall('^F.+:',x) # crea un a lista con elementos que empiece por F hata encontrar el ultimo :
print(y)

#ejercicio 3 

print('\nencontrar e imprimir los caracteres que esten entre "F" y el primer ":"\n')

y = re.findall('^F.+?:',x) # crea una lista con los elementos que empiecen por F y cualquier caraxter hasta llegar al primer : que encuentre 
print(y)

# ejercicio 4

print('\nextraer del documento mbox-short.txt todos los correos mencionados\n')

hand = open('archivos_planos/mbox-short.txt')
for line in hand:
	line = line.rstrip() # quita el doble espacio al analizar los datos
	y = re.findall('\S+@\S+',line) # Crean una lista para cada objeto quue encuetra con las caracteristicas 
	if len(y) > 0 :
		print(y)

# Ejercicio 4 encontrar e imprimir los correos que primero tengan el prefijo From
print('\nencontrar los correos madres\n')
hand = open('archivos_planos/mbox-short.txt')
for line in hand:
	line = line.rstrip() # quita el doble espacio al analizar los datos
	y = re.findall('^From (\S+@\S+)',line) # Crean una lista para cada objeto quue encuetra con las caracteristicas 
	if len(y) > 0 :
		print(y)

 # ejercicio 5 extraer los dominios de los Emails anteriores

print('\nextraer los dominios de los correos anteriores\n')
hand = open('archivos_planos/mbox-short.txt')
for line in hand:
	line = line.rstrip() # quita el doble espacio al analizar los datos
	y = re.findall('^From .*@([^ ]*)',line) # Crean una lista para cada objeto quue encuetra con las caracteristicas 
	if len(y) > 0 :
		print(y)

# ejercicio 6 omprimir el numero maximo de spam confidence 

print('\nExtraer el numero mayor de spam confidence:\n')

hand = open('archivos_planos/mbox-short.txt')
numlist = list()

for line in hand:
	line =line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(stuff) != 1 :
		continue
	num = float(stuff[0])
	numlist.append(num)
#print(numlist)	
print('numero maximo:', max(numlist))
