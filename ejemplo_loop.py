#bucle simple
n = 5
while n > 0 :
    print(n)
    n = n - 1
print("blastoff!!")
print(n)

# detener bucle con break

while True:
    line = input(">")
    if line == "done" :
        break
    print(line)
print("done!")

# ejemplo continue y break

while True:
    line = input(">")
    if line[0] == "#" :
        continue
    if line == "done" :
        break
    print(line)
print("done!")
    

