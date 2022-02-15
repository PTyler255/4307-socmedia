import sqlite3
import sys

# ./reply.py user_id post_id reply_id "[full content of comment]"


def reply(user, post, repl, content):
    con = sqlite3.connect('blueit.db')
    cur = con.cursor()
    cur.execute('INSERT INTO likes (user_id, post_id, content) VALUES (?, ?, ?)', [user, post, repl, content])
    con.commit()
    con.close()

def main():
    (user, post, repl, content) = sys.argv[1:5]
    reply(user, post, repl, content)

if __name__ == "__main__":
    main()
