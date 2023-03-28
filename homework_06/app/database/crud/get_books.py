from database import db
from sqlalchemy.orm import joinedload

from ..models import Author, Book


def get_books():
    library = db.session.query(
        Book
    ).options(
        joinedload(Book.authors).
        subqueryload(Author.books)
    ).all()

    return library
