import urllib.request, urllib.parse, urllib.error

# para leer un dato de una pagina web desde python

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	print(line.decode().strip())

# para decodificar los datos de una pagina web y contar la cantidad de palabras repatidas

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
	words =line.decode().split()# decodifica de UTF-8 a cadena de caracteres Uncode-string
	for word in words:
 		counts[word] = counts.get(word,0)+1
print(counts)

#para obtener los datos de una pagina en codigo HTML

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
	print(line.decode().strip())


# obtener datos de una pagina web con beautifulsoup

from bs4 import BeautifulSoup
import ssl

#para ignorar los errores por certificados ssl

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url).read()
soup =BeautifulSoup(html,'html.parser')

# resive todos los datos precedidos de <a
tags = soup('a')
for tag in tags:
	print(tag.get('href',None))

###########################################################
#codigo para ignorar errores de certificado SSL 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode =ssl.CERT_NONE


#url = input('Enter -')
url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url,context =ctx).read()
soup =BeautifulSoup(html,'html.parser')

# resive todos los datos precedidos de <a
tags = soup('span',class_='comments')
for tag in tags:
	print(tag.get("comments",None))

#codigo para ignorar los errores en certificados SSL
