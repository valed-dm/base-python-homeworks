from ..db import db

author_book = db.Table(
    "author_book",
    db.Column("author_id", db.Integer, db.ForeignKey("authors.id"), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey("books.id"), primary_key=True),
)
