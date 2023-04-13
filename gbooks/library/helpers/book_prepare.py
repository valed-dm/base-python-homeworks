from api.schemas import Book
from library.models import Book as Book_DB


def book_prepare(book: Book_DB) -> Book:
    authors = [auth.name for auth in book.authors.all()]
    categories = [cat.name for cat in book.categories.all()]

    book_data = Book(
        authors=authors,
        categories=categories,
        date=book.date,
        description=book.description,
        google_book_id=book.google_book_id,
        image_src=book.image_src.image_src,
        title=book.title,
        rubric=book.rubric,
        remark=book.remark
    )

    return book_data
