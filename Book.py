import sqlite3

class Book:

    def __init__(self):
        self.__db_name = "db.db"
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS books(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title VARCHAR(255) NOT NULL,
                       genre VARCHAR(255) NOT NULL
                       )
                ''')
        connection.commit()
        connection.close()
    
    def create(self, title: str, genre: str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (title, genre) VALUES (?, ?)", (title, genre))
        connection.commit()
        connection.close()
    
    def list(self):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        connection.close()
        return books
    
    def getSingleByTitle(self, title: str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        book = cursor.fetchone()
        connection.close()
        return book
    
    def delete(self, title: str):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE title = ?", (title,))
        connection.commit()
        connection.close()


