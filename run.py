import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('SELECT * from urls')

print("<html>")
for r in c.fetchall():
    url = r[0]
    tag = r[1]
    print('<img src="{}" style="width:400px">'.format(url))

print("</html>")


