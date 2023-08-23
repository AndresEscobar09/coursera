#imprimir un elemento de la lista

friends = ['Joseph','Glen','Sally']
print(friends[1])

# canbiar un valor de la lista

nums = [1,54,67,89,46,22,12]
print(nums)
nums[1] = 'Hola'
nums[5] = 'mundo'
print(nums)

#saber la longitud de unA lista

print(len(nums))
print(range(len(nums)))
print(range(4))

#recorrar una lista con for

for i in range(len(nums)) :
    num = nums[i]
    print('number:',num)

#imprimir un rango de elementos dentro de la lista

print(nums[1:3])imprime desde la posicion 1 hasta la 3-1
