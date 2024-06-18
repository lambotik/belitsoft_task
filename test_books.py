import sqlite3

from datetime import datetime
from conftest import Queries

now_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def test_create_db(create_table):
    db = create_table
    book = ('Garry', 'Potter', 2012)
    Queries.insert_books(book)