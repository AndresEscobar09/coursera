import re

hand = open('archivos_planos/mbox-short.txt')
for line in hand:
	line = line.rstrip() # quita el doble espacio al analizar los datos
	if re.search('^From: ',line): # el ^ indica que se comprara solo los que esten al principio de la linea
		print(line)

# De la forma comun seria:

print('\nde la forma comun:\n')
hand = open('archivos_planos/mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From: ') >= 0:
		print(line)

# otra forma seria:

print('\nOtra Forma es:\n')
hand = open('archivos_planos/mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From:'): #comprueba si la cadena comnienza con...
		print(line)


# ejerciop para especificar aun mas la busqueda.

print('\nimprime solo las lines que tengan X- al inicio segido por varios caracteres que NO sean espacio y termina en ":"\n')

hand = open('archivos_planos/mbox-short.txt')
for line in hand:
	line = line.rstrip() # quita el doble espacio al analizar los datos
	if re.search('^X-\S+:',line): # re.serch busca en una cadena coincidencias y ('\S+:') indica "seguido de cualquier caracter que no se ESPACIO" 
		print(line)