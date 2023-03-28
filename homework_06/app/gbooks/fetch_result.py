from . import fetch_uri_create, data_prepare, fetch_books
from .helpers import sorting_results
from .schemas import Book


def fetch_result(title: str, pace: str, category: str, sort: str):
    books = []
    books_found = "0"

    if title:
        uri = fetch_uri_create(title, pace)
        res = fetch_books(uri)

        books_found = res[0]
        books_raw_data = res[1]

        for item in books_raw_data:
            book = Book(*data_prepare(item))
            books.append(book)

    books = sorting_results(books, category, sort)

    return [books_found, books]
