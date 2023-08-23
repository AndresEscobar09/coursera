import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ingore SSl certificate Errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verrify_mode =ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1812508.html'
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html,'html.parser')

#manipular los datos
numbers = []
tags = soup.find_all('span', class_='comments') # se buscan en la etiqueta <span> que tiene la clase 'comments', el metodo fin_all devueve una lista con los elementos que coinciden 
for tag in tags:
	try:
		number =int(tag.text.strip())# span.text se utiliza para para obtener los caracteres dentro de la etiqueta span y strip() para eliminar los espacios.
		numbers.append(number)
	except ValueError:
		pass
print(numbers)
total = 0
for number in numbers:
	total = total + number

print('the sum for all numbers is:',total )



