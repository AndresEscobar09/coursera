fname = input('enter file name:\n')
fh =open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    #print(line)
    stuff = line.split()
     #print(stuff)
    for w in stuff:
        if w in lst:
            continue
        else:
            lst.append(w)
lst.sort()
print(lst)
   