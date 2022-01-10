from django.shortcuts import render

from book import models


def books(request):
    book = models.Post1.objects.all()
    return render(request, 'book_list.html', {'books': book})
