from django import forms
from django.shortcuts import redirect, render
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
        
        
def create_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():                 # ✅ validation/sanitization here
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/book_form.html", {"form": form})