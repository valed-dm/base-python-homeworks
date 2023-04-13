from django.contrib import messages


def info_add(request, book_title):
    messages.info(request, f"'{book_title}' was successfully added to library.")
