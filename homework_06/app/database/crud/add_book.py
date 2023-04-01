from flask import flash, redirect, url_for
from sqlalchemy import exists

from database import db
from gbooks.helpers import authors_string
from ..models import Author, Book, Category, Image


def add_book(book, rubric, remarks):
    b = book
    authors = authors_string(b.authors)
    id_exists = db.session.query(
        exists().
        where(Book.google_book_id == b.google_book_id)). \
        scalar()

    # prepares book data to be filled in books table
    if not id_exists:
        book_to_library = Book(
            authors_str=authors,
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
        db_authors = db.session.query(Author).all()
        db_authors = [item.name.lower() for item in db_authors]
        for author in b.authors:
            if author.lower() not in db_authors:
                author_for_book = Author(name=author)
                db.session.add(author_for_book)

        # fills in the category table
        db_categories = db.session.query(Category).all()
        db_categories = [item.name for item in db_categories]
        for category in b.categories:
            if category not in db_categories:
                category_for_book = Category(name=category)
                db.session.add(category_for_book)

        # fills in the book-author association table
        db_authors = db.session.query(Author).all()
        db_authors = [
            author for author in db_authors if author.name in b.authors
        ]
        for author in db_authors:
            book_to_library.authors.append(author)

        # fills in the book-category association table
        db_categories = db.session.query(Category).all()
        db_categories = [
            category for category in db_categories if category.name in b.categories
        ]
        for category in db_categories:
            book_to_library.categories.append(category)

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
