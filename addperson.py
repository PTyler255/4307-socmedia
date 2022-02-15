import sqlite3
import sys

# ./addperson.py name username

(name, username) = sys.argv[1:3]

con = sqlite3.connect('blueit.db')
cur = con.cursor()

cur.execute('INSERT INTO people (name, username) VALUES (?, ?)', [name, username])
con.commit()
con.close()