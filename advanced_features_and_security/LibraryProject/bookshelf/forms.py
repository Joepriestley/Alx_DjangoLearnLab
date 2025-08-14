from django import forms
from django.shortcuts import redirect, render
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
        
        
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():                 # ✅ validation/sanitization here
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})