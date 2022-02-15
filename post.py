import sqlite3
import sys

# ./post.py user_id "[full content of post]"


def post(user, content):
    con = sqlite3.connect('blueit.db')
    cur = con.cursor()
    cur.execute('INSERT INTO post (user_id, content) VALUES (?, ?)', [user, content])
    con.commit()
    con.close()

def main():
    (user, content) = sys.argv[1:3]
    post(user, content)

if __name__ == "__main__":
    main()
