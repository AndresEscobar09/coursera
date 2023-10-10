import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqllite')#crea el archivo como base de datos
cur =conn.cursor()


#se crea las tablas user, course y la tabla de conexion de todos con todos member que tiene dos claves foraneas

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;                  

CREATE TABLE User (     
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  name TEXT UNIQUE

 );
CREATE TABLE Course (
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  title TEXT UNIQUE

 );
CREATE TABLE Member (
                  user_id INTEGER,
                  course_id INTEGER,
                  role INTEGER,
                  PRIMARY KEY (user_id, course_id)

 )
 

                  ''')

fname = input('enter file name')
if len(fname)< 1:
    fname = 'archivos_planos/roster_data.json'


str_data = open(fname).read()
json_data =json.loads(str_data) #se convierte  en una matriz de matrices

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print((name,title,role))

    cur.execute('''INSERT OR IGNORE INTO user (name) VALUES (?)''',(name, )) #agrega el nombre en la base ced datos si este no se encuetra repetido 
    cur.execute('SELECT id FROM User WHERE name = ? ',(name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id,role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()


 



    


