
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from .forms import ExampleForm
from .models import Book
# Create your views here.

def create_book(request):
    if request.method =="POST":
        form= ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        
    else:
        form = ExampleForm()
    return render(request,'bookshelf/create_book.html', {'form':form})

def book_list(request):

    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create' , raise_exception=True)
def can_create(request):
    #logic here 
    pass
    return render(request, 'bookshelf/create_book.html')
@permission_required('bookshelf.can_edit' , raise_exception=True)
def can_edit(request,pk):
    book = get_object_or_404(Book,pk)
    #logic here 
    pass
    return render(request, 'bookshelf/edit_book.html')
@permission_required('bookshelf.can_delete' , raise_exception=True)
def can_delete(request,pk):
    book=get_object_or_404(Book, pk)
    #logic here 
    pass
    return render(request, 'bookshelf/delete_book.html')

@permission_required('bookshelf.can_view' , raise_exception=True)
def can_view(request):
    #logic here 
    pass
    return render(request, 'bookshelf/view.html')


def search_books(request):
    q = request.GET.get("q", "").strip()
    qs = Book.objects.none()
    if q:
        qs = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
    return render(request, "bookshelf/search_results.html", {"books": qs, "q": q})
