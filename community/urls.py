from django.urls import path
from . import views
app_name ="community"
urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('book/borrow/<int:book_id>/', views.book_borrow, name='book_borrow'),
    path('book/listmng/',views.book_listmng, name='book_listmng'),
    path('book/listmng/sign/<int:borrow_id>/', views.book_listmng_sign, name='book_listmng_sign'),
    path('book/listmng/sign/del/<int:borrow_id>/', views.book_listmng_sign_del, name='book_listmng_sign_del'),
    path('download/', views.file_download, name='file_download'),
]
