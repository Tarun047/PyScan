import sqlite3
import datetime
import ast


class Loader:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("""iData.db""")
            try:
                c = self.conn.cursor()
                c.execute("""SELECT * FROM VTAB""")
            except sqlite3.OperationalError:
                c.execute("""CREATE TABLE VTAB(HASH STRING,RESP STRING,DETECT INTEGER,PRIMARY KEY(HASH))""")
            self.conn.commit()
        except sqlite3.OperationalError:
            print("""Insufficient Previlages, Make Sure to Run App as Admin""")

    def insert(self, hash, response,detect):
        try:
            c = self.conn.cursor()
            c.execute("""INSERT INTO VTAB VALUES(?,?,?)""", [hash, str(response),detect])
        except sqlite3.OperationalError as e:
            c.execute("""CREATE TABLE VTAB(HASH STRING,RESP STRING,DETECT INT,PRIMARY KEY(HASH))""")
            c.execute("""INSERT INTO VTAB VALUES(?,?,?)""", [hash, str(response),detect])
            debug = open('log.txt', "a")
            debug.write(str(datetime.datetime.now()), e, e.__cause__(), sep=' # ')
            debug.close()
        self.conn.commit()

    def query(self, Hash):
        c = self.conn.cursor()
        try:
            s = next(c.execute("""SELECT RESP FROM VTAB WHERE HASH = ?""", (Hash,)))
            return ast.literal_eval(s[0])

        except StopIteration:
            return None
    def retrieveAll(self):
        c = self.conn.cursor()
        for row in c.execute("""SELECT * FROM VTAB"""):
            print(row)
    def cleanAll(self):
        c = self.conn.cursor()
        c.execute("""DELETE FROM  VTAB""")
        self.conn.commit()
