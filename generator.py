from dataclasses import dataclass

from faker import Faker

fake = Faker()


@dataclass
class Book:
    title: str = None
    author: str = None
    year: int = None


def generate_fake_book():
    title = fake.catch_phrase()
    author = fake.name()
    year = int(fake.year())
    book = (title, author, year)
    yield book
