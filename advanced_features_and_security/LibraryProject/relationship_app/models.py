from django.db import models
from django.contrib.auth.models import AbstractUser, User



#Extending the User model using the 1to1 method
class UserProfile(models.Model):
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('librarian','Librarian'),
        ('member','Member')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length= 30, choices=ROLE_CHOICES, default='member')
    
    def __str__(self):
        return f"{self.user.username}, ({self.role})"


class CustomUser(AbstractUser):
    date_of_birth= models.DateField()
    profile_image =models.ImageField()
    
class Author(models.Model):
    name =models.CharField(max_length=100)

class Book(models.Model):
    title= models.CharField(max_length=150)
    author= models.ForeignKey(Author,on_delete=models.CASCADE)
    
    class Meta:
        permissions=[
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
    
        ]
class Library(models.Model):
    name= models.CharField(max_length=100) 
    books= models.ManyToManyField(Book)
    
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library =models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name