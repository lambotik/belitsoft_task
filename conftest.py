import sqlite3

import pytest

import generator
from queries import Queries


@pytest.fixture
def table():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS books(
                BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title VARCHAR(255) NOT NULL,
                Author VARCHAR(255) NOT NULL,
                Year INTEGER NOT NULL);''')
        database.commit()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        assert 'books' in tables[0], 'Table books has not been created.'
        print("The table has been successfully created.")
        yield database
        cursor.close()


@pytest.fixture
def fill_the_table(table):
    db = table
    for i in range(10):
        new_book = next(generator.generate_fake_book())
        Queries.insert_books(new_book)
