import urllib.request
import json

base_url = "http://py4e-data.dr-chuck.net/json?"

def obtener_place_id(direccion):
    parametros = {'address': direccion, 'key': '42'}
    url_completa = base_url + urllib.parse.urlencode(parametros)

    try:
        respuesta = urllib.request.urlopen(url_completa).read().decode()
        datos_json = json.loads(respuesta)
        
        if 'status' in datos_json and datos_json['status'] == 'OK':
            place_id = datos_json['results'][0]['place_id']
            return place_id
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Solicitar la ubicación al usuario
ubicacion = input("Ingrese una ubicación: ")

# Obtener el place_id
place_id = obtener_place_id(ubicacion)

if place_id:
    print("El place_id de", ubicacion, "es:", place_id)
else:
    print("No se pudo obtener el place_id para la ubicación:", ubicacion)