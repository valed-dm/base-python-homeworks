from .author_book import author_book
from ..db import db


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    books = db.relationship("Book", secondary=author_book, back_populates="authors")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r})'
