from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import list_books, LibraryDetailView

Urlspatterns=[
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('register/', views.register, name='register'),
    path('admin/',views.admin_view,name='admin_view'),
    path('member/' views.member_vies, name='member_view'),
    path('edit_book/<int:pk>/', views.can_change_book, name='change_book'),
    path('add_book/',views.can_add_book, name ='add_book'),
    path('delete_book/<int:pk>/', views.can_delete_book, name ='delete_book'),
  
]