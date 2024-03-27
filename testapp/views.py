from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = "testapp/book_detail.html"
    context_object_name = "book"