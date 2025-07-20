from django.urls import path
from . import views


Urlspatterns=[
    path('books/', views.book_list),
    path('library/', views.bookDetail.as_view())
]