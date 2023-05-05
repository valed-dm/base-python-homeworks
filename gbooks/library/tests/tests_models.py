from django.test import TestCase

from api.schemas import Book
from library.crud import get_or_create
from library.models import Author, Book as Book_DB, Category, Image


class SetUpTestData(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        book = Book()
        authors = get_or_create(Author, book.authors)
        categories = get_or_create(Category, book.categories)
        image_src = Image(image_src=book.image_src)
        image_src.save()
        book_to_library = Book_DB(
            authors_str=book.authors[0],
            title=book.title,
            description=book.description,
            date=book.date,
            google_book_id=book.google_book_id,
            rubric="read_asap",
            remark="no remark added",
            image_src=image_src,
        )
        book_to_library.save()
        book_to_library.authors.set(authors)
        book_to_library.categories.set(categories)


class TestBookModel(SetUpTestData):

    def setUp(self):
        self.book = Book_DB.objects. \
            prefetch_related("authors", "categories"). \
            get(pk=1)

    def test_book_str(self):
        expected_object_name = repr(self.book.title)
        self.assertEqual(str(self.book), expected_object_name)

    def test_book_authors_str_label(self):
        field_label = self.book._meta.get_field("authors_str").verbose_name
        self.assertEqual(field_label, "authors str")

    def test_book_authors_str_max_length(self):
        max_length = self.book._meta.get_field("authors_str").max_length
        self.assertEqual(max_length, 200)

    def test_book_title_label(self):
        field_label = self.book._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_book_title_max_length(self):
        max_length = self.book._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_book_description_label(self):
        field_label = self.book._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_book_description_field_type(self):
        field_type = self.book._meta.get_field("description").get_internal_type()
        self.assertEqual(field_type, "TextField")

    def test_book_date_label(self):
        field_label = self.book._meta.get_field("date").verbose_name
        self.assertEqual(field_label, "date")

    def test_book_date_field_type(self):
        field_type = self.book._meta.get_field("date").get_internal_type()
        self.assertEqual(field_type, "DateField")

    def test_book_google_book_id_label(self):
        field_label = self.book._meta.get_field("google_book_id").verbose_name
        self.assertEqual(field_label, "google book id")

    def test_book_google_book_id_max_length(self):
        max_length = self.book._meta.get_field("google_book_id").max_length
        self.assertEqual(max_length, 20)

    def test_book_google_book_id_field_is_set_unique(self):
        field_unique = self.book._meta.get_field("google_book_id").unique
        self.assertEqual(field_unique, True)

    def test_book_rubric_label(self):
        field_label = self.book._meta.get_field("rubric").verbose_name
        self.assertEqual(field_label, "rubric")

    def test_book_rubric_max_length(self):
        max_length = self.book._meta.get_field("rubric").max_length
        self.assertEqual(max_length, 20)

    def test_book_remark_label(self):
        field_label = self.book._meta.get_field("remark").verbose_name
        self.assertEqual(field_label, "remark")

    def test_book_remark_max_length(self):
        max_length = self.book._meta.get_field("remark").max_length
        self.assertEqual(max_length, 100)

    def test_book_image_src_label(self):
        field_label = self.book._meta.get_field("image_src").verbose_name
        self.assertEqual(field_label, "image src")

    def test_book_image_src_value(self):
        self.assertEqual(self.book.image_src.image_src, "/static/img/no_cover.webp")

    def test_book_authors_label(self):
        field_label = self.book._meta.get_field("authors").verbose_name
        self.assertEqual(field_label, "authors")

    def test_book_authors_value(self):
        self.assertEqual(self.book.authors.all()[0].name, "-no author-")

    def test_book_categories_label(self):
        field_label = self.book._meta.get_field("categories").verbose_name
        self.assertEqual(field_label, "categories")

    def test_book_categories_value(self):
        self.assertEqual(self.book.categories.all()[0].name, "-no category-")

    def test_book_fields_qty(self):
        self.assertEqual(len(self.book._meta.fields), 9)

    def test_book_fields_many_to_many_qty(self):
        self.assertEqual(len(self.book._meta.many_to_many), 2)


class TestAuthorModel(SetUpTestData):

    def setUp(self):
        self.author = Author.objects.get(pk=1)

    def test_author_str(self):
        expected_object_name = repr(self.author.name)
        self.assertEqual(str(self.author), expected_object_name)

    def test_author_name_label(self):
        field_label = self.author._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_author_name_max_length(self):
        max_length = self.author._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)

    def test_author_name_is_set_unique(self):
        field_unique = self.author._meta.get_field("name").unique
        self.assertEqual(field_unique, True)

    def test_author_value(self):
        self.assertEqual(self.author.name, "-no author-")

    def test_author_fields_qty(self):
        self.assertEqual(len(self.author._meta.fields), 2)

    def test_author_fields_many_to_many_qty(self):
        self.assertEqual(len(self.author._meta.many_to_many), 0)


class TestCategoryModel(SetUpTestData):

    def setUp(self):
        self.category = Category.objects.get(pk=1)

    def test_category_str(self):
        expected_object_name = repr(self.category.name)
        self.assertEqual(str(self.category), expected_object_name)

    def test_category_name_label(self):
        field_label = self.category._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_category_name_max_length(self):
        max_length = self.category._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)

    def test_category_name_is_set_unique(self):
        field_unique = self.category._meta.get_field("name").unique
        self.assertEqual(field_unique, True)

    def test_category_value(self):
        self.assertEqual(self.category.name, "-no category-")

    def test_category_fields_qty(self):
        self.assertEqual(len(self.category._meta.fields), 2)

    def test_category_fields_many_to_many_qty(self):
        self.assertEqual(len(self.category._meta.many_to_many), 0)


class TestImageModel(SetUpTestData):

    def setUp(self):
        self.image = Image.objects.get(pk=1)

    def test_image_str(self):
        expected_object_name = repr(self.image.image_src)
        self.assertEqual(str(self.image), expected_object_name)

    def test_image_src_label(self):
        field_label = self.image._meta.get_field("image_src").verbose_name
        self.assertEqual(field_label, "image src")

    def test_image_src_max_length(self):
        max_length = self.image._meta.get_field("image_src").max_length
        self.assertEqual(max_length, 200)

    def test_image_src_field_type(self):
        field_type = self.image._meta.get_field("image_src").get_internal_type()
        self.assertEqual(field_type, "CharField")

    def test_image_fields_qty(self):
        self.assertEqual(len(self.image._meta.fields), 2)
