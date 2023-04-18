from django.shortcuts import render, get_object_or_404
# Create your views here.

from .models import Book

def index(request):
    book_list = Book.objects.order_by('title')
    context = {'book_list' : book_list}
    return render(request, 'community/book_list.html', context)