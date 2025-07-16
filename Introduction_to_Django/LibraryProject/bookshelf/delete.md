# deleting from table
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# output:
(1, {'bookshelf.Book': 1})
# book deleted successfully