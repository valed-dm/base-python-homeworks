from flask import flash, redirect, url_for
from sqlalchemy import exists
from sqlalchemy import func
from sqlalchemy import select

from database import db
from gbooks.helpers import authors_string
from ..models import Author, Book, Category, Image


def add_book(book, rubric, remarks):
    b = book
    book_authors = [author.strip().lower() for author in b.authors]
    book_categories = [category.strip().lower() for category in b.categories]
    authors_str = authors_string(book_authors)
    id_exists = db.session.query(
        exists().
        where(Book.google_book_id == b.google_book_id)). \
        scalar()

    # prepares book data to be filled in books table
    if not id_exists:
        book_to_library = Book(
            authors_str=authors_str,
            title=b.title,
            description=b.description,
            date=b.date,
            google_book_id=b.google_book_id,
            rubric=rubric,
            remarks=remarks,
            # fills in the images table
            image_src=Image(url=b.image_src),
        )

        # fills in the authors table
        authors_lower = db.session.scalars(select(func.lower(Author.name))).all()
        for author in book_authors:
            if author not in authors_lower:
                author_for_book = Author(name=author.title())
                db.session.add(author_for_book)

        # fills in the category table
        categories_lower = db.session.scalars(select(func.lower(Category.name))).all()
        for category in book_categories:
            if category not in categories_lower:
                category_for_book = Category(name=category.title())
                db.session.add(category_for_book)

        # fills in the book-author association table
        book_auth = db.session.query(Author).filter(func.lower(Author.name).in_(book_authors))
        for auth in book_auth:
            book_to_library.authors.append(auth)

        # fills in the book-category association table
        book_cat = db.session.query(Category).filter(func.lower(Category.name).in_(book_categories))
        for cat in book_cat:
            book_to_library.categories.append(cat)

        # sends all new data to all 6 tables in "gbooks" db at once
        db.session.add(book_to_library)
        db.session.commit()

        flash(
            f"'{b.title}' was added to '{rubric}' with '{remarks}'",
            category="success"
        )
        return redirect(url_for("book", book=b))

    else:
        flash(
            f"'{b.title}': --- This book already exists in the library ---",
            category="info"
        )
        return redirect(url_for("book", book=b))
