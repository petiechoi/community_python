from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.contrib import messages
from .forms import BookForm, BorrowForm
from .models import Book, Borrow
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
def index(request):
    book_list = Book.objects.order_by('title')
    context = {'book_list' : book_list}
    return render(request, 'community/book_list.html', context)

@csrf_exempt
def book_borrow(request, book_id):
    """
    도서 대여
    """
    """
    최초에 else(GET) 로 빈 폼을 전달함. render
    그리고 폼 전송을 하면 POST로 저장되서 redirect 됨.
    """
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.book = book
            borrow.manager = request.user
            borrow.save()
            return redirect('index')
    else:
        form = BorrowForm()

    context = {'form' : form, 'book' : book}
    return render(request, 'community/book_form.html', context)