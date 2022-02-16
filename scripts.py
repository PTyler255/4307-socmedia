import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor, row):
        d[col[0]] = row[idx]
    return d

class socialDB:

    def __init__(self):
        self.con = sqlite3.connect('blueit.db')
        self.con.row_factory = dict_factory 
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.commit()
        self.con.close()

    def addperson(self, name, username): 
        self.cur.execute('INSERT INTO people (name, username) VALUES (?, ?)', [name, username])

    def comment(self, user, post, content):
        self.cur.execute('INSERT INTO likes (user_id, post_id, content) VALUES (?, ?, ?)', [user, post, content])

    def following(self, from_un, following_un):
        from_id = self.un2id(from_un)
        from_id = self.un2id(following_un)
        self.cur.execute('INSERT INTO following (from_id, following_id) VALUES (?, ?)', [from_id, following_id])

    def getFeed(self, user, count):
        self.cur.execute('SELECT * FROM following JOIN post ON following_id = post.user_id WHERE from_id = ? ORDER BY post.date_created DESC LIMIT ?', [user, count])
        feed = self.cur.fetchall()
        return feed

    def getComments(self, post):
        self.cur.execute('SELECT * FROM following JOIN post ON following_id = post.user_id WHERE from_id = ? ORDER BY post.date_created DESC', [post, post])
        '''
        WITH RECURSIVE replies( parent, main, level ) AS (
             SELECT reply_id, id, 0
             FROM comments
             WHERE reply_id IS NULL AND post_id = ?
            UNION
             SELECT replies.main, comments.id, replies.level+1
             FROM comments JOIN replies
             ON replies.main = comments.reply_id
             WHERE comments.post_id = ?
             ORDER BY 2 DESC, date_created DESC
        )
        SELECT user_id, content, date_created, level
        FROM replies JOIN comments
        ON main = comment.id;
        '''
        comments = self.cur.fetchall()
        return comments

    def like(self, user, post):
        self.cur.execute('INSERT INTO likes (user_id, post_id) VALUES (?, ?)', [user, post])

    def post(self, user, content):
        self.cur.execute('INSERT INTO post (user_id, content) VALUES (?, ?)', [user, content])

    def reply(self, user, post, repl, content):
        self.cur.execute('INSERT INTO likes (user_id, post_id, reply_id, content) VALUES (?, ?, ?, ?)', [user, post, repl, content])

    def un2id(self, un):
        self.cur.execute('SELECT from_id FROM people WHERE username = ?', [un]) 
        ide = self.cur.fetchone()
        return ide

