numero = 0
total = 0.0
while True :
    entrada = input('ingrese numero\n')
    if entrada == 'done' :
        break
    try :
        entrada = float(entrada)
    except :
        print('entrada invalida')
        continue
    numero = numero + 1
    total = total + entrada
print(total,numero,total/numero)
