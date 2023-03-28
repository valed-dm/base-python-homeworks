from flask import flash


def info_sort_library(rubric, category, author, sort):
    if rubric is None:
        flash(f"Library shown in lifo order.", category="success")
    else:
        flash(f"Library filtered with params: ", category="success")
        flash(f"rubric: {rubric}, category: {category}", category="success")
        flash(f"author: {author}, sort: {sort}", category="success")
