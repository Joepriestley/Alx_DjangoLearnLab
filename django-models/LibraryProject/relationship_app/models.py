from django.db import models
from django.contrib.auth.models import User



#creating  user with built-in User model
user =User.objects.create_user('joseph','joeamonoo1114@gmail.com', 'priestleyjoe1')


#Retrieve user 
user=User.objects.get(username="joseph")
# Create your models here.
class Author(models.Model):
    name =models.CharField(max_length=100)

class Book(models.Model):
    title= models.CharField(max_length=150)
    author= models.ForeignKey(Author,on_delete=models.CASCADE)
class Library(models.Model):
    name= models.CharField(max_length=100) 
    books= models.ManyToManyField(Book)
    
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library =models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name