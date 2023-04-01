import os

import redis
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask_migrate import Migrate
from flask_session.__init__ import Session
from flask_wtf import CSRFProtect

from database import db
from database.crud import get_books, get_book, add_book, del_book, get_authors
from gbooks import fetch_result, get_args, get_args_library, sort_books
from gbooks import info_search, info_delete, info_sort_library

config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
app.config['SESSION_REDIS'] = redis.from_url(app.config['SESSION_REDIS'])

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)
sess = Session()
sess.init_app(app)


@app.get("/", endpoint="index")
def index_view():
    args = get_args(request)
    books_found, books = fetch_result(*args)
    # stores books data received from api request into redis storage
    for book in books:
        session_key = book.google_book_id
        session[session_key] = book
    info_search(args, books_found, len(books))

    return render_template("books.html", books_found=books_found, books=books)


@app.route("/book/", methods=["GET", "POST"], endpoint="book")
def book_view():
    if "title" in request.args:
        # when a new search starts from the 'book' endpoint:
        title, pace, category, sort = get_args(request)
        return redirect(f"/?title={title}&pace={pace}&category={category}&sort={sort}")

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


@app.get("/library/", endpoint="library")
def library_view():
    args = request.args
    authors = get_authors()
    if "del_book" in args:
        google_book_id = args.get("del_book")
        del_book(google_book_id)
        # to display deleted book title gets book data from redis storage
        book = session.get(google_book_id)
        if book:
            info_delete(book.title)
            # gets books data from db
    library_books = get_books()
    rubric, category, author, sort = get_args_library(request)
    if "rubric" in args:
        library_books = sort_books(rubric, category, author, sort, library_books=library_books)
    info_sort_library(rubric, category, author, sort)

    return render_template("library_books.html", authors=authors, books=library_books)


@app.get("/library/book/", endpoint="library_book")
def library_book_view():
    if "rubric" in request.args:
        # when library sorting asked from the 'library_book' endpoint:
        rubric, category, author, sort = get_args_library(request)
        return redirect(f"/library/?rubric={rubric}&category={category}&author={author}&sort={sort}")

    book_id = request.args.get("book_id")
    authors = get_authors()
    # gets book data from db
    book = get_book(book_id)

    return render_template("library_book.html", authors=authors, book=book)


if __name__ == "__main__":
    app.run(host="0.0.0.0")