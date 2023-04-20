from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Borrow(models.Model):
    borrower = models.CharField(max_length=10)
    borrow_date = models.DateTimeField()
    manager = models.ForeignKey(User, on_delete=models.PROTECT, max_length=10)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.borrower