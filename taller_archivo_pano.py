#pasar rodo un archivo plano a letras mayusculas

fname = input('Enter file name:\n')
try:
    fh =open(fname)
except:
    print('file cannot be opened')
    quit()
for line in fh :
    line = line.upper()
    line = line.rstrip()
    print(line)
