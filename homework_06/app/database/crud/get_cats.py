from database import db
from ..models import Category


def get_cats():
    db_cats = db.session.query(Category).all()
    db_cats = sorted([item.name for item in db_cats])

    return db_cats
