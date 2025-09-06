from django.urls import path
from .views import BookAPIView

from . import views 

urlpatterns = [
    path("api/books", views.BookAPIView.as_view(), name="book_list_create"),
]
