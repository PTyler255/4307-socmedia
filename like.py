import sqlite3
import sys

# ./like.py user_id post_id


def like(user, post):
    con = sqlite3.connect('blueit.db')
    cur = con.cursor()
    cur.execute('INSERT INTO likes (user_id, post_id) VALUES (?, ?)', [user, post])
    con.commit()
    con.close()

def main():
    (user, post) = sys.argv[1:3]
    like(user, post)

if __name__ == "__main__":
    main()
