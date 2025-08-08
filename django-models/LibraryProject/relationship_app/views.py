
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Book,Author,Librarian
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,CreateView

from .models import Library


# Create your views here.
def list_books(request):
    books= Book.objects.all()
    context={'book_list':books}
    return render(request, 'relationship_app/list_books.html',context)
#class based view to render books in library
class LibraryDetailView(DetailView):
    model= Library
    template_name = 'relationship_app/library_detail.html'

#CBV FOR USER REGISTRATION
# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/register.html'
    
def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login')
    else:
        form =UserCreationForm()
    return render(request,'register.html',{'form':form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

 

    
    

    
    
    