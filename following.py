import sqlite3
import sys

# ./following.py my_username their_username


def follow(from_id, following_id):
    con = sqlite3.connect('blueit.db')
    cur = con.cursor()
    cur.execute('INSERT INTO following (from_id, following_id) VALUES (?, ?)', [from_id, following_id])
    con.commit()
    con.close()

def main():
    (from_id, following_id) = sys.argv[1:3]
    follow(from_id, following_id)

if __name__ == "__main__":
    main()