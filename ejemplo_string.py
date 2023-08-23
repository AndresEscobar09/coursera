fruit = 'banana'
print(fruit)
letter = fruit[1]
print(letter)

x = 3
w = fruit[x-1]
print(w)

print(len(fruit))


# ciclo while para recorrer un string

index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index,letter)
    index =index + 1

# ciclo for para recorrer un string

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
x = 0
for letra in fruit: # la variable que recorre debe ser nueva y unica.
    print(x,letra)
    x = x + 1
    
#para imprimir un string por partes 

s = 'Monty Python'
print(s)
print(s[0:4])
print(s[6:7])
print(s[6:20])


# buscar letras en string

'n' in fruit

if 'n' in fruit :
    print("great")

# pasar todo el string a minuscula

fruit = "BanaNa"
print(fruit)
y = fruit.lower()
print(y)

#encontrar la posicion de un caracter 

x = fruit.find('na')
print(x)

x = fruit.find('x')
print(x)



# todas mayusculas

fruit = fruit.upper()
print(fruit) 

#buscar y remplazar

greet = '    hello bob        '
print(greet)
nstr = greet.replace('bob','jane')
print(nstr)

nstr = greet.replace('e','X')
print(nstr)

# espacios
print(greet.lstrip())

print(greet.rstrip())

print(greet.strip())


#greet.twist()
#greet.startswith()

#greet.join()
#greet.split()

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])