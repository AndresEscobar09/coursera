import re
hand = open('archivos_planos/regex_sum_1812506.txt')
numlist = list()
total = 0
for line in hand:
	line =line.rstrip()
	y = re.findall('[0-9]+', line)
	if len(y) > 0:
		for i in range(0,len(y)):
			num = int(y[i])
			numlist.append(num)
#print(numlist)

for num in numlist:
	total += num
print(total)

#http://py4e-data.dr-chuck.net/regex_sum_42.txt