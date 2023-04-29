"""
URL configuration for gbooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from api.views import books_view, book_view
from library.views import BookDetailView, LibraryListView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("admin/", admin.site.urls),
    path("", books_view, name="books"),
    path("book/", book_view, name="book"),
    path("library/", LibraryListView.as_view(), name="library"),
    path("library/book/<slug:slug>", BookDetailView.as_view(), name="library_book"),
]
