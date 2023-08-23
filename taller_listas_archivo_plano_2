fname = input('enter fine name\n')
fln = open(fname)
count = 0

for line in fln:
    line = line.rstrip() 
    if not line.startswith('From '): 
        continue
    words = line.split() 
    print(words[1])
    count += 1
print('There were',count,'lines in the file with From as the first word')

    
    

