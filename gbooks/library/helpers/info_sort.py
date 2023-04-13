from django.contrib import messages


def info_sort_library(request, r):
    if r.rubric is None:
        messages.info(request, f"Library shown in fifo order:")
    else:
        messages.info(request, f"Library filtered with params: ")
        messages.info(request, f"rubric: {r.rubric}, category: {r.category}")
        messages.info(request, f"author: {r.author}, sort: {r.sort}")
