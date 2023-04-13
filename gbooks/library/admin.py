from django.contrib import admin

from library.models import Author, Book, Category, Image

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Image)
