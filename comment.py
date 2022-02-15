import sqlite3
import sys

# ./post.py user_id post_id "[full content of comment]"


def comment(user, post, content):
    con = sqlite3.connect('blueit.db')
    cur = con.cursor()
    cur.execute('INSERT INTO likes (user_id, post_id, content) VALUES (?, ?, ?)', [user, post, content])
    con.commit()
    con.close()

def main():
    (user, post, content) = sys.argv[1:4]
    comment(user, post, content)

if __name__ == "__main__":
    main()
