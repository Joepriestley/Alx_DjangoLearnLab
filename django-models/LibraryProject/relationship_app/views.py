from django.shortcuts import render
from .models import Book,Author,Librarian,Library


# Create your views here.
def book_list(request):
    books= Book.objects.all()
    context={'book_list':books}
    return render(request, context)
    
    
    