import sqlite3
import sys

# ./following.py my_username their_username

(from_id, following_id) = sys.argv[1:3]

con = sqlite3.connect('blueit.db')
cur = con.cursor()

cur.execute('INSERT INTO following (from_id, following_id) VALUES (?, ?)', [from_id, following_id])
con.commit()
con.close()