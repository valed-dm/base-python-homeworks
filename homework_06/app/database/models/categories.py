from .category_book import category_book
from ..db import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    books = db.relationship("Book", secondary=category_book, back_populates="categories")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r})'