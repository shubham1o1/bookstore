import sqlite3

class Database:

    def __init__(self,db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Title text, author text, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        # self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        # conn.commit()
        rows = self.cur.fetchall()
        # self.conn.close()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author =? OR year = ? OR isbn = ?",(title,year,author,isbn))
        rows = self.cur.fetchall()
        # self.conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?",(id,))
        self.conn.commit()
        # self.conn.close()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title,author,year,isbn,id))
        self.conn.commit()
        # self.conn.close()

    def __del__(self):
        self.conn.close()
