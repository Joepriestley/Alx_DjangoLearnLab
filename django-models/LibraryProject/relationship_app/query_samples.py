from relationship_app.models import  Book,Librarian, Library, Author

book=Book.objects.all(author="George Orwell")

library = Library.objects.