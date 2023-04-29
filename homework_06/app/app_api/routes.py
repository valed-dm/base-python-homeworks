from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session

from database.crud import add_book
from gbooks import fetch_result, get_args_book
from gbooks import info_search

bp = Blueprint('api', __name__)


@bp.route("/", endpoint="index")
def index_view():
    r = get_args_book(request)
    books_found, books = fetch_result(r)
    # stores books data received from api request into redis storage
    for book in books:
        session_key = book.google_book_id
        session[session_key] = book
    info_search(r, books_found, len(books))

    return render_template("books.html", books_found=books_found, books=books)


@bp.route("/book/", methods=["GET", "POST"], endpoint="book")
def book_view():
    if "title" in request.args:
        # when a new search starts from the 'book' endpoint:
        r = get_args_book(request)
        return redirect(f"/?title={r.title}&pace={r.pace}&category={r.category}&sort={r.sort}")

    elif "google_book_id" in request.args:
        google_book_id = request.args.get("google_book_id")
        # gets book data from redis storage
        book = session.get(google_book_id)
        if request.method == "POST":
            rubric = request.form.get("rubric")
            rubric = "read_asap" if rubric == "all" or rubric == "read_asap" else rubric
            remarks = request.form.get("remarks")
            add_book(book, rubric, remarks)

        return render_template("book.html", book=book)
