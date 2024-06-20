import random
from pprint import pprint
import allure

import generator
from queries import Queries
@allure.epic('Sqlite task.')
class TestTasks:
    @allure.title('Add books.')
    def test_check_book_is_added(self, table):
        for _ in range(10):
            new_book = next(generator.generate_fake_book())
            Queries.insert_books(new_book)
            all_books = Queries.select_book(new_book)
            assert new_book in all_books, 'The new book was not added to the database.'

    @allure.title('Obtaining a list of all books.')
    def test_check_all_books(self, table, fill_the_table):
        all_books = Queries.select_all_books()
        # pprint(all_books)
        count_books = Queries.count_all_books()
        assert len(all_books) == count_books, 'Something went wrong.'

    @allure.title('Obtaining information about the book on ID (positive).')
    def test_get_information_by_id_positive(self, table):
        random_id = random.randint(1, 10)
        result = Queries.get_book_information_by_id(random_id)
        assert result != [], 'Books with such ID are not in the database.'

    @allure.title('Obtaining information about the book on ID (negative).')
    def test_get_information_by_id_negative(self, table):
        book_id = 999
        result = Queries.get_book_information_by_id(book_id)
        assert result == [], 'Books with such ID are not in the database.'

    @allure.title('Updating information about the book on ID.')
    def test_update_information_by_id(self, table):
        new_data = next(generator.generate_fake_book())
        random_id = random.randint(1, 20)
        result = Queries.update_book_information_by_id(random_id, new_data)
        book_after_update = Queries.get_book_information_by_id(random_id)
        assert new_data == book_after_update[0]
    @allure.title('Removing the book on ID.')
    def test_delete_book_by_id(self, table):
        books_data = Queries.data_from_the_table()
        list_books_id_before = [i[0] for i in books_data]
        positive_value_id = random.choice(list_books_id_before)
        Queries.delete_book_by_id(positive_value_id)
        books_data = Queries.data_from_the_table()
        list_books_id_after = [i[0] for i in books_data]
        assert positive_value_id not in list_books_id_after, 'The book on ID was not deleted.'
    @allure.title('Delete all information from the table.')
    def test_clear_table(self, table):
        result = Queries.clear_table()
        assert result == [], 'The table was not cleaned.'