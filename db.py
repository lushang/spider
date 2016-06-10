__author__ = 'Robert'
import sqlite3


class SpiderDb():
    conn = None
    c = None
    def __init__(self):
        self.conn = sqlite3.connect('spider.db')
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def createdb(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS words (word text, frequency real)''')
        self.conn.commit()

    # the param words should be type of dict
    def addword(self, words):
        self.c.execute("SELECT * FROM words")
        rows = self.c.fetchall()
        olddict = dict(rows)

        for word in words:
            if word in olddict:
                frequency = words[word] + olddict[word]
                self.c.execute("UPDATE words SET frequency =? WHERE text =?", (frequency, word))
            else:
                frequency = words[word]
                self.c.execute("INSERT INTO words VALUES (?,?)", (word, frequency))
        self.conn.commit()

    def getwords(self):
        self.c.execute("SELECT * FROM words")
        return self.c.fetchall()

