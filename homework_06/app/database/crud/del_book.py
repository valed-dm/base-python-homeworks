from database import db, Book


def del_book(google_book_id):
    b = db.one_or_404(db.select(Book).filter_by(google_book_id=google_book_id))
    db.session.delete(b)
    db.session.commit()
