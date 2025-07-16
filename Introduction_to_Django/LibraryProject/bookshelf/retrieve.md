# Query all attributs of Book instance 
from bookshelf.models import Book
Book.objects.get(title="1984")
# Expected Output:
# <Book: Book object (2)>

