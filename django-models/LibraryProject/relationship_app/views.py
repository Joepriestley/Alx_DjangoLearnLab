from django.shortcuts import render
from .models import Book,Author,Librarian
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Library


# Create your views here.
def book_list(request):
    books= Book.objects.all()
    context={'book_list':books}
    return render(request, 'relationship_app/list_books.html',context)
#class based view to render books in library
class bookDetail(DetailView):
    model= Library
    template_name = 'relationship_app/library_detail.html'
    
    
    