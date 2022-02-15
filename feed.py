import sqlite3
import sys

# ./post.py user_id "[full content of post]"


def feed(user):
    con = sqlite3.connect('blueit.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM following JOIN post ON following_id = post.user_id WHERE from_id = ? ORDER BY post.date_created DESC', [user])
    posts = cur.fetchall()
    con.commit()
    con.close()
    return posts

def main():
    (user) = sys.argv[1]
    posts = feed(user)
    for post in posts[:20]:
        print(post)

if __name__ == "__main__":
    main()

'''
SELECT *
FROM following JOIN post
ON following_id = post.user_id
WHERE from_id = ?
ORDER BY post.date_created DESC
'''
