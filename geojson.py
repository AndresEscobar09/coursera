import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'# se debe poner el signo ? para que los espacios que se ingresen desde el teclado de conviertan en +

while True:
	address = input('Enter Location:\n')
	if len(address) < 1 : break

	url = serviceurl + urllib.parse.urlencode({'address': address})# adiere los datos de address a la URL para realizar la busqueda

	print('Retrieving', url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('retrieved:', len(data),'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] != 'OK':
		print('=== failure to retrieve ===')
		print(data)
		continue

	print(json.dumps(js,indent=4))
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]

	print('lat',lat,'lng',lng)
	location = js['results'][0]['formatted_address']
	print(location)
	

	

