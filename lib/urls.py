#lib/urls.py
from django.urls import path
from . import views

app_name='lib'
urlpatterns = [
    path('',views.index,name='index'),
    path('platformt/', views.platformt, name='platformt'),
    path('detail/',views.detail,name='detail'),
    path('detail_queue/',views.detail_queue,name='detail_queue'),
    path('addBook/',views.addBook,name='addBook'),
    path('delBook/<int:book_id>',views.deleteBook,name='delBook'),
   # path('platformt/',views.platformt,name='platformt'),
]