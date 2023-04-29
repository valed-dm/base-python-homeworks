from .author_book import author_book
from .category_book import category_book
from ..db import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    authors_str = db.Column(db.String(200), nullable=True, default="", server_default="")
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True, default="", server_default="")
    date = db.Column(db.Date, nullable=False, default="1900-01-01", server_default="1900-01-01")
    google_book_id = db.Column(db.String(30), nullable=False, unique=True)
    rubric = db.Column(db.String(20), nullable=False)
    remarks = db.Column(db.String(100), nullable=True, default="", server_default="")

    image_src = db.relationship(
        "Image",
        backref="books",
        uselist=False,
        cascade="all",
        lazy="selectin"
    )
    authors = db.relationship(
        "Author",
        secondary=author_book,
        back_populates="books",
        lazy="selectin"
    )
    categories = db.relationship(
        "Category",
        secondary=category_book,
        back_populates="books",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Book '{self.title}'>"
