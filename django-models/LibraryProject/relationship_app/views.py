
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import  permission_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import Book,Author,Librarian
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,CreateView

from .models import Library

#role checking function for admin role

def is_admin(user):
    """
    Check if the user has an admin role.
    """
    if hasattr(user, 'role'):
        return user.role == 'admin'
    if hasattr(user, 'profile'):
        return user.profile.role == 'admin'
    return False
#role checking function for admin role with passes_test decorator 
@user_passes_test(is_admin,login_url='login',redirect_field_name=None)
def admi_view(request):
    return render(request,'relationship_app/admin_view.html')

#role checking function for Librarian 
def is_librarian(user):
    if hasattr(user, 'role'):
        return user.role =='librarian'
    if hasattr(user,'profile'):
        return user.profile.role =='librarian'
    
#check for it to pass test
@user_passes_test(is_librarian, login_url='login',redirect_field_name =None)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#role checking function for member
def is_member(user):
    
    if hasattr(user,'role'):
        user.role =='member'
    if hasattr(user, 'profie'):
        return user.profile.role == 'member'
#check for will be 

@user_passes_test(is_member, login_url='login',redirect_field_name='None')
def member_view(request):
    return render(request,'relationship_app/member_view.html')
        

# Create your views here.
def list_books(request):
    books= Book.objects.all()
    context={'book_list':books}
    return render(request, 'relationship_app/list_books.html',context)

#checking for permission to add, edit ,change or delete book
@permission_required('relationship_app.can_add_book',raise_exception=True)
def can_add_book(request):
     if request.method=='POST':
        #add logic here 
        pass
    
        return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception = True)
def can_change_book(request, pk):
    book= get_object_or_404(Book,pk=pk)
    if request.method=='POST':
        #add logic here 
        pass
    return render(request,'relationship_app/edit_book.html', {'book':book})

@permission_required('relationship_app.can_delete_book', raise_exception= True)
def can_delete_book(request, pk):
    book =get_object_or_404(Book,pk=pk)
    if request.method=='POST':
        book.delete()
    return redirect('book_list')

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
    return render(request,'relationship_app/register.html',{'form':form})


class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

 

    
    

    
    
    