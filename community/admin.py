from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']       # Book 모델의 title로 검색 기능

admin.site.register(Book, BookAdmin)   # 장고 Admin에서 모델 관리하기
