from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.contrib import messages
from .forms import BookBorrowForm
from .models import Book
from django.utils import timezone

def index(request):
    book_list = Book.objects.order_by('title')
    context = {'book_list' : book_list}
    return render(request, 'community/book_list.html', context)

def book_borrow(request, book_id):
    """
    도서 대여
    """
    """
    최초에 else(GET) 로 빈 폼을 전달함. render
    그리고 폼 전송을 하면 POST로 저장되서 redirect 됨.
    """

    messages.error(request, 'zzzzzzzzz')
    if request.method == 'POST':
        form = BookBorrowForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.borrow_date = timezone.now()
            book.save()
            return redirect('community:index')
    else:
        book = get_object_or_404(Book, pk=book_id)
        messages.error(request, book_id, book.title)
        if book.title:
            form = BookBorrowForm(instance=book)
        else:
            form = BookBorrowForm()

    context = {'form' : form}
    return render(request, 'community/book_form.html', context)