from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, redirect

from library.helpers import info_delete
from library.models import Book


# deletes from reverse side of 1-2-1 Image relation
@receiver(post_delete, sender=Book)
def delete_image(sender, instance, **kwargs):
    instance.image_src.delete()


def delete_book(request):
    delete_id = request.GET.get("del", None)
    book = get_object_or_404(Book, google_book_id=delete_id)
    title = book.title
    book.delete()
    info_delete(request, title)

    return redirect("library/books")
