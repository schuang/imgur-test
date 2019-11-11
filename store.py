#!/usr/bin/env python3

import sqlite3
import argparse
import os

db_filename = 'data.db'
db_table = 'urls'
file_dir = 'images/'

def add_to_db(url=None, tag=''):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls (url text, tag text)''')
    c.execute("INSERT INTO " + db_table + " ('url', 'tag') VALUES (?,?)", (url,tag))
    conn.commit()
    conn.close()

def del_url(url=None, tag=''):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute("DELETE FROM " + db_table + " where url = ?", (url,))
    try:
        fpath = os.path.join(file_dir, os.path.basename(url))
        print("trying to delete ",fpath," ...")
        os.remove(fpath)
    except:
        pass
    conn.commit()
    conn.close()


def run():
   parser = argparse.ArgumentParser()
   parser.add_argument("--add", "-a", help="add an URL")
   parser.add_argument("--tag", "-t", help="add a tag", default='funny')
   parser.add_argument("--delete", "-d", help="delete an URL")
   args = parser.parse_args()

   if args.add:
      print("adding URL...")
      add_to_db(args.add, args.tag)
   if args.delete:
      print("deleting URLs")
      del_url(args.delete, args.tag)

if __name__ == '__main__':
    run()
