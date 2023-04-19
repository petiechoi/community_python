from django import forms
from community.models import Book

class BookBorrowForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['borrower']