import xml.etree.ElementTree as ET #importamos la libreria xml y la aopdamos ET
data = '''<person>
	<name>Chuck</name>
	<phone type="intl">
			+1 734 303 4456
		</phone>
		<email hide="yes"/>
</person>'''
tree =ET.fromstring(data)
print('Name',tree.find('name').text)# el metodo tree.find busca en la etiqueta name y extrae lo que tiene (en este caso "Chuck")
print('Attr:',tree.find('email').get('hide')) # extrae lo que se encuentra en la etiqueta email dentro del atributo hide  


# ejemplo 2

input = '''<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x="7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>

	<phone type="intl">
			+1 734 303 4456
		</phone>
		<email hide="yes"/>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:',len(lst))

for item  in lst:
	print('name:',item.find('name').text)
	print('ID:',item.find('id').text)
	print('Attribute',item.get("x"))

