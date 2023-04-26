from django import forms
from community.models import Book, Borrow

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher']
        labels = {
            'title' : '책 제목',
            'author' : '저자',
            'publisher' : '출판사',
        }

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['borrower']
        labels = {
            'borrower' : '이름',
        }

# class BookBorrowForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['borrower']
#         labels = {
#             'borrower' : '대여자',
#         }