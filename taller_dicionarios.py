name = input('Enter file:\n')
if len(name) < 1:
    name = 'archivos_planos\mbox-short.txt'
handle = open(name)
count = dict()
add = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    word  = words[1]
    count[word] = count.get(word,0) + 1
most_word = None
most_count = None

for word,value in count.items():
    if most_count is None or value > most_count:
        most_word = word
        most_count = value
print(most_word,most_count)


    