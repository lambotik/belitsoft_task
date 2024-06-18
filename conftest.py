import sqlite3
import pytest


@pytest.fixture
def create_table():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
        BookID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title VARCHAR(255) NOT NULL,
        Author VARCHAR(255) NOT NULL,
        Year INTEGER NOT NULL);''')
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        assert 'books' in tables[0], 'Table books has not been created.'
        print("The table has been successfully created.")
        yield cursor
        cursor.execute('''DELETE FROM books where BookID > 0''')
        cursor.execute('''select * from books''')
        db_after_deleting = cursor.fetchall()
        assert db_after_deleting == [], 'Database is not empty.'
        cursor.close()


class Queries:
    @staticmethod
    def insert_books(book_data):
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            cursor.execute('''INSERT INTO books (Title, Author, Year) 
            VALUES (?, ?, ?);''', book_data)
            print(f"The book is added: {book_data}.")
            database.commit()
