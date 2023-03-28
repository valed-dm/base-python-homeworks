from database import db
from ..models import Author


def get_authors():
    db_authors = db.session.query(Author).all()
    db_authors = sorted([item.name for item in db_authors])

    return db_authors
