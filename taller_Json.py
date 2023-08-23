import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_1812511.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
datos = dict()
datos = info
#print(datos)
valores_numericos = []

for dato in datos['comments']:
	valores_numericos.append(int(dato['count']))

print(valores_numericos)
total = 0

for valor in valores_numericos:
	#	print(valor)
	total = total + valor
print('sum:',total)

