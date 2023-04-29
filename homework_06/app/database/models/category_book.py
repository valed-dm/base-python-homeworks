from ..db import db

category_book = db.Table(
    "category_book",
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey("books.id"), primary_key=True),
)