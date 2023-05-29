# from django.shortcuts import render
# from . import models
#
#
# def book_list(request):
#     book = models.Book.objects.all()
#     return render(request, 'booklist.html', {'book': book)
from django.shortcuts import render
from . import models


def book_list(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})