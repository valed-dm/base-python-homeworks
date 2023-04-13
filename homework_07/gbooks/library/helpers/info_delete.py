from django.contrib import messages


def info_delete(request, book_title):
    messages.info(request, f"'{book_title}' was successfully deleted from library.")
