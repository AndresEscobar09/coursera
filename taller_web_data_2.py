import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verrify_mode =ssl.CERT_NONE
repetir = int(input('Enter count:\n'))
posicion = int(input('Enter position:\n'))



url = 'http://py4e-data.dr-chuck.net/known_by_Baighley.html'

def estract_url(url_encontrada):

	html = urllib.request.urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html,'html.parser')

	tags = soup.find_all('a') # sustrae todos los elementos que esten dentro de la etiqueta <a

	

	lista =[]
	for tag in tags:
		lista.append(tag['href'])# agrega a la lista los elementos qu se encuetren en la clase href
	url_ext = lista[posicion-1]
	return url_ext

for i in range(repetir+1 ):
	print('Retrieving: ',url)
	url = estract_url(url)
	
	