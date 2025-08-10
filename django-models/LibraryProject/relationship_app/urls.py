from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import list_books, LibraryDetailView, 

Urlspatterns=[
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('register/', views.register, name='register'),
    path('admin/',views.admin_view,name='admin_view'),
    path('member/' views.member_vies, name='member_view'),
    path('book/<int:pk>/edit', views.can_change_book, name='change_book'),
    path('book/add',views.can_add_book, name ='add_book'),
    path('book/<int:pk>/delete', views.can_delete_book, name ='delete_book'),
  
]