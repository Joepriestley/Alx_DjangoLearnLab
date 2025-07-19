from relationship_app.models import  Book,Librarian, Library, Author
# Query all books by a specific author
author=Author.objects.get(name=author_name)
book=Book.objects.filter(author=author)

# Listing all books in a library.
library = Library.objects.get(name=library_name)
library.books.all()
# Retrieve the librarian for a library
Librarian.objects.get(library= "library_name")