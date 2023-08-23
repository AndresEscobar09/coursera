#contar las lineas en un archibo plano
x = open('archivos_planos/hola.txt')#esta es la ruta del archivo partiendo desde el archivo de codigo.
print(x.read())
x = open('archivos_planos/hola.txt')
count = 0  
for line in x:
    count = count + 1
    print(line)
print(count,'lineas')


#contador de caracteres.
x = open('archivos_planos/hola.txt')
inp = x.read()
print(len(inp))

#imprimir solo caracteres de una ubicacion
print(inp[:11]) #tener en cuenta que los \n cuentan como un caracter
print(inp[15:22])

# buscar una palabra en el archibo.
x = open('archivos_planos/hola.txt')
for line in x:
    if line.startswith('hola') :
        print(line)
        
#para quitar el doble espacio podemos usar

x = open('archivos_planos/hola.txt')
for line in x:
    line =line.rstrip()
    if line.startswith('hola') :
        print(line)

#para buscar palabras que contengan algunos caracteres

x = open('archivos_planos/hola.txt')
for line in x :
    line =line.rstrip()
    if not 'n' in line :
        continue
    print(line)
#para que el usuario ingrese la ruta del archivo.
while True:
    
    x = input('enter the file name:\n')
    try:
        y = open(x)
    
    except :
        print('file cannot be opened')
        continue
    count = 0
    for line in y :
        if line.startswith('hola') :
            count = count + 1
    print('there were',count,' subject lines in', y)
    