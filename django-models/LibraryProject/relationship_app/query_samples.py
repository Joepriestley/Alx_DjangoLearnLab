from relationship_app.models import  Book,Librarian, Library, Author
# Query all books by a specific author
author=author=Author.objects.gets(name="author_name")
book=Book.objects.all(author=author)

# Listing all books in a library.
library = Library.objects.get(name=library_name)
library.books.all()

# Retrieving the librarian for a library.
library.librarian

#Or
# Librarian.objects.get(name="name", library_name="lib_name")