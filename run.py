import sqlite3
import os

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('SELECT * from urls')

print("<html>")
for r in c.fetchall():
    url = r[0]
    tag = r[1]
    filename, ext = os.path.splitext(url)

    if ext in ['.mp4', '.ogg', 'webm']:
       #print('<source src="{}" style="width:200px">'.format(url))
       print('<video height="200" controls><source src="{}" type="video/{}">no browser support</video>'.format(url,ext[1:]))
    else:
       print('<img src="{}" style="height:200px">'.format(url))

print("</html>")


