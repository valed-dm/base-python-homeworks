from flask import flash


def info_delete(book_title):
    flash(f"'{book_title}' was successfully deleted from library.", category="success")
