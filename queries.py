import sqlite3

import allure


class Queries:
    @staticmethod
    def insert_books(book_data: tuple):
        """
        Insert books into table.
        :param book_data:
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('INSERT book INTO  table "books"'):
                ...
            cursor.execute('''
            INSERT INTO books (Title, Author, Year) 
            VALUES (?, ?, ?);''', book_data)
            print(f"The book is added: {book_data}.")
            database.commit()

    @staticmethod
    def select_book(book: tuple):
        """
        Return book information.
        :param book: (Title, Author, Year)
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('SELECT Title, Author, Year FROM books'):
                ...
            cursor.execute(f'''
            select Title, Author, Year from books
            where (Title, Author, Year) == {book};''')
            result = cursor.fetchall()
            return result

    @staticmethod
    def select_all_books():
        """
        Return Title, Author, Year about all books in the table.
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('SELECT Title, Author, Year from books'):
                ...
            cursor.execute(f'''
            select Title, Author, Year from books''')
            books = cursor.fetchall()
            return books

    @staticmethod
    def count_all_books():
        """
        Return amount books in the table.
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('SELECT count(BookID) from books where BookID > 0'):
                ...
            cursor.execute('''
            select count(BookID) from books
            where BookID > 0''')
            count = cursor.fetchall()
            return count[0][0]

    @staticmethod
    def get_book_information_by_id(book_id: int):
        """
        Return information about of the book by BookID.
        :param book_id:
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('SELECT Title, Author, Year from books where BookID == {book_id}'):
                ...
            cursor.execute(f'''
            select Title, Author, Year from books
            where BookID == {book_id}''')
            result = cursor.fetchall()
            print('Information about the book for ID:', result)
            return result

    @staticmethod
    def update_book_information_by_id(book_id: int, new_data: tuple):
        """
        Update book information by BookID.
        :param book_id:
        :param new_data:
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('UPDATE books SET (Title, Author, Year) = {new_data} WHERE BookID == {book_id};'):
                ...
            cursor.execute(f'''
            update books
            set (Title, Author, Year) = {new_data}
            where BookID == {book_id};''')
            database.commit()
            print('Information about book has been successfully updated.')

    @staticmethod
    def clear_table():
        """
        Delete all information from the table.
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('DELETE FROM books where BookID > 0;'):
                ...
            cursor.execute('''DELETE FROM books where BookID > 0;''')
            database.commit()
            with allure.step('UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = "books";'):
                ...
            cursor.execute('''UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = "books";''')
            database.commit()
            with allure.step('SELECT * FROM books;'):
                ...
            cursor.execute('''select * from books;''')
            result = cursor.fetchall()
            # print(result)
            return result

    @staticmethod
    def data_from_the_table():
        """
        Return all information from the table.
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('SELECT BookID, Title, Author, Year FROM books;'):
                ...
            cursor.execute('''select BookID, Title, Author, Year from books;''')
            result1 = cursor.fetchall()
            books_list = [i for i in result1]
            # print(books_list)
        return books_list

    @staticmethod
    def delete_book_by_id(book_id: int):
        """
        Delete book information from the table by BookID.
        :param book_id:
        :return:
        """
        with sqlite3.connect('database.db') as database:
            cursor = database.cursor()
            with allure.step('DELETE FROM books WHERE BookID'):
                ...
            cursor.execute(f'''DELETE FROM books where BookID == {book_id};''')
            database.commit()
