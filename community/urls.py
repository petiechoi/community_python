from django.urls import path
from . import views
app_name ='community'
urlpatterns = [
    path('', views.index),
    path('book/borrow/<int:book_id>/', views.book_borrow, name='book_borrow'),
]