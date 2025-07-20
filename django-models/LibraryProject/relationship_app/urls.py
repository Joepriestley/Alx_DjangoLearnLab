from django.urls import path
from .views import list_books,LibraryDetailView


Urlspatterns=[
    path('books/', views.list_books, name='books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail')
]