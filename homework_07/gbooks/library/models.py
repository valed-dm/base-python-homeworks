from django.db import models


# m-2-m
class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name!r}"


# m-2-m
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name!r}"


# 1-2-1
class Image(models.Model):
    image_src = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.image_src!r}"


# m-2-m
class Book(models.Model):
    authors_str = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    date = models.DateField(default="1900-01-01")
    google_book_id = models.CharField(max_length=20, unique=True)
    rubric = models.CharField(max_length=20)
    remark = models.CharField(max_length=100, blank=True, default="")
    image_src = models.OneToOneField(Image, null=True, related_name="images", on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title!r}"
