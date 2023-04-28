from api.helpers import sorting_results
from api.schemas import Book
from .fetch_books import fetch_books
from .fetch_prepare import data_prepare
from .fetch_uri import fetch_uri_create


def fetch_result(r):
    books = []
    books_found = "0"

    if r.title:
        uri = fetch_uri_create(r.title, r.pace)
        res = fetch_books(uri)

        books_found = res[0]
        books_raw_data = res[1]

        for item in books_raw_data:
            api_data = data_prepare(item)
            book = Book(
                authors=api_data.authors,
                categories=api_data.categories,
                date=api_data.date,
                description=api_data.description,
                google_book_id=api_data.google_book_id,
                image_src=api_data.image_src,
                title=api_data.title
            )
            books.append(book)

    books = sorting_results(books, r.category, r.sort)

    return [books_found, books]
