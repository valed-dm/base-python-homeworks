from database import db, Book as Book_db
from gbooks.schemas import Book


def get_book(book_id):
    b = db.get_or_404(Book_db, book_id)

    book = Book(
        authors=b.authors,
        categories=b.categories,
        date=b.date,
        description=b.description,
        google_book_id=b.google_book_id,
        image_src=b.image_src.url,
        title=b.title
    )

    return book
