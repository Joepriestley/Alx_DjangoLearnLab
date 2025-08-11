from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('member/', views.member_view, name='member_view'),
    path('edit_book/<int:pk>/', views.can_change_book, name='change_book'),
    path('add_book/', views.can_add_book, name='add_book'),
    path('delete_book/<int:pk>/', views.can_delete_book, name='delete_book'),
]
