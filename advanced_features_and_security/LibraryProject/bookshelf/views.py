from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,get_object_or_404


# Create your views here.
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
