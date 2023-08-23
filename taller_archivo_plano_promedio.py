fname = input('Enter file name:\n')
try:
    fh = open(fname)
except:
    print('file cannot be opened')
    quit()
    
count = num = add = 0
    
for line in fh :

    if 'X-DSPAM-Confidence:' in line:
        count = count + 1
        line = line.rstrip()
        num = float(line[20:26])
        add = add + num
print('Average spam confidence:',add/count)


