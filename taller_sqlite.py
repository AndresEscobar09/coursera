import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('email_counts.sqlite')
cur = conn.cursor()

# Crear la tabla si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')

# Nombre del archivo mbox.txt que contiene los correos electrónicos
archivo_mbox = "archivos_planos/mbox.txt"

try:
    # Abrir el archivo mbox.txt
    with open(archivo_mbox, 'r') as file:
        # Iterar a través de las líneas del archivo
        for linea in file:
            # Buscar direcciones de correo electrónico en el formato "From: email@organizacion.com"
            if linea.startswith("From: "):
                direccion = linea.split()[1]  # Obtener la dirección de correo electrónico
                dominio = direccion.split('@')[1]  # Obtener el dominio

                # Verificar si el dominio ya existe en la base de datos y actualizar el recuento
                cur.execute('SELECT count FROM Counts WHERE org = ?', (dominio,))
                row = cur.fetchone()
                if row is None:
                    cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (dominio,))
                else:
                    cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (dominio,))

        # Confirmar los cambios en la base de datos
        conn.commit()

except FileNotFoundError:
    print(f"El archivo {archivo_mbox} no se encontró.")

# Obtener y mostrar los resultados
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC')

print("Organización\tRecuento de Correos Electrónicos")
for row in cur.fetchall():
    print(row[0], "\t", row[1])

# Cerrar la conexión a la base de datos
cur.close()
