import sqlite3
import sys

# ./addperson.py name username

def addperson(name, username):
    con = sqlite3.connect('blueit.db')
    cur = con.cursor()
    cur.execute('INSERT INTO people (name, username) VALUES (?, ?)', [name, username])
    con.commit()
    con.close()

def main():
    (name, username) = sys.argv[1:3]
    addperson(name, username)
    
if __name__ == "__main__":
    main()