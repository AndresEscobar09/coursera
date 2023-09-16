import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
            DROP TABLE IF EXISTS Counts''')

cur.execute('''
            CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('enter file name')
if(len(fname)<1):
    fname = 'archivos_planos/mbox-short.txt'
fh = open(fname)

# blucle de busqueda en el TXT
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT Count FROM Counts WHERE email = ?',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''
                    INSERT INTO Counts (email,count) VALUES (?, 1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
    conn.commit()
#https://www.sqlite.org/lang_select.html

sqlstr = 'SELECT email, count FROM Counts ORDER BY Count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()