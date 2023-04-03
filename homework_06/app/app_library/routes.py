from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session

from database.crud import get_books, get_book, del_book, get_authors, get_cats
from gbooks import info_delete, info_sort_library, sort_books, get_args_library

bp = Blueprint('lib', __name__)


@bp.route("/library/", endpoint="library")
def library_view():
    args = request.args
    authors = get_authors()
    cats = get_cats()
    if "del_book" in args:
        google_book_id = args.get("del_book")
        del_book(google_book_id)
        # to display deleted book title gets book data from redis storage
        book = session.get(google_book_id)
        if book:
            info_delete(book.title)
            # gets books data from db
    library_books = get_books()
    r = get_args_library(request)
    if "rubric" in args:
        library_books = sort_books(r, library_books=library_books)
    info_sort_library(r)

    return render_template("library_books.html", authors=authors, cats=cats, books=library_books)


@bp.route("/library/book/", endpoint="library_book")
def library_book_view():
    if "rubric" in request.args:
        # when library sorting asked from the 'library_book' endpoint:
        r = get_args_library(request)
        return redirect(f"/library/?rubric={r.rubric}&category={r.category}&author={r.author}&sort={r.sort}")

    book_id = request.args.get("book_id")
    authors = get_authors()
    # gets book data from db
    book = get_book(book_id)

    return render_template("library_book.html", authors=authors, book=book)
