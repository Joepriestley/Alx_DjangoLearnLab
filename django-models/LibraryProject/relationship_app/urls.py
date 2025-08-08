from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import list_books,LibraryDetailView,RegisterView

Urlspatterns=[
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
  
]