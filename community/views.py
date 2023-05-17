from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .forms import BookForm, BorrowForm
from .models import Book, Borrow
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
def index(request):
    page = request.GET.get('page', '1') # 페이지
    book_list = Book.objects.order_by('title')
    paginator = Paginator(book_list, 10)
    page_obj = paginator.get_page(page)
    context = {'book_list' : page_obj }
    return render(request, 'community/book_list.html', context)

#@csrf_exempt

def book_borrow(request, book_id):
    """
    도서 대여
    """
    """
    최초에 else(GET) 로 빈 폼을 전달함. render
    그리고 폼 전송을 하면 POST로 저장되서 redirect 됨.
    """

    """
    동시 대여에 대한 코드작성 필요
    """
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.book = book
            borrow.state=False
            borrow.save()
            return redirect('index')
    else:
        form = BorrowForm()

    context = {'form' : form, 'book' : book}
    return render(request, 'community/book_form.html', context)

"""
도서 관리 리스트(관리자전용)
"""
@login_required(login_url='common:login')
@staff_member_required
def book_listmng(request):
    page = request.GET.get('page', '1') # 페이지
    Borrowlist = Borrow.objects.order_by('borrow_date')
    paginator = Paginator(Borrowlist, 10)
    page_obj = paginator.get_page(page)
    context = {'borrowlist': page_obj}
    return render(request, 'community/book_listmng.html', context)


"""
도서 관리 체크(관리자전용)
"""
@login_required(login_url='common:login')
@staff_member_required
def book_listmng_sign(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    if borrow.state == False :
        borrow.state = True
        borrow.borrow_date = timezone.now()
        borrow.manager = request.user
        borrow.save()
    else :
        borrow.delete()
    return redirect('community:book_listmng')

def book_listmng_sign_del(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    borrow.delete()
    return redirect('community:book_listmng')

