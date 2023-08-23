import json

data = ''' { 
	"name" : "Chuck",
	"phone" : {
		"type" : "intl",
		"number" : "+1 734 303 4456"
	},
	"email" : {
	"hide" : "yes"
	}
}'''

info = json.loads(data) # trae los datos y los convierte en un diccionario de python
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

import json
# extraer todos los datos que concuerden con name,id y 'x'
input = '''
[
	{"id" : "001",
		"x" : "2",
		"name" : "Chuck" 
	},
	{"id" : "009",
		"x" :"7",
		"name" : "Pam"
	}
]'''

info = json.loads(input)
print('User count:', len(info))
print(info)

for item in info:
	print('Name:', item['name'])
	print('Id:', item['id'])
	print('Attribute:', item['x'])