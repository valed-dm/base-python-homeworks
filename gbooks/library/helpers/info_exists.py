from django.contrib import messages


def info_exists(request, book_title):
    messages.info(request, f"'{book_title}' already exists in the library.")
