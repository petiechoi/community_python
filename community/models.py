from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    borrower = models.CharField(max_length=10, null=True, blank=True)
    borrow_date = models.DateTimeField(null=True, blank=True)
    manager = models.ForeignKey(User, on_delete=models.PROTECT ,max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title

