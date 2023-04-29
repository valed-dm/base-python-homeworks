from flask import flash


def info_sort_library(r):
    if r.rubric is None:
        flash(f"Library shown in fifo order.", category="success")
    else:
        flash(f"Library filtered with params: ", category="success")
        flash(f"rubric: {r.rubric}, category: {r.category}", category="success")
        flash(f"author: {r.author}, sort: {r.sort}", category="success")
