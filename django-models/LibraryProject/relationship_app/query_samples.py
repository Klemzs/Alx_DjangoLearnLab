import os
import sys
import django

# Get the absolute path to the project root (where manage.py is)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create some sample data first
def create_data():
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter 1", author=author1)
    book2 = Book.objects.create(title="Harry Potter 2", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    
    # Create library and add books
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2, book3)
    
    # Create librarian
    Librarian.objects.create(name="John Doe", library=library)

create_data()

# Query 1: All books by specific author
print("1. All books by J.K. Rowling:")
books = Book.objects.filter(author__name="J.K. Rowling")
for book in books:
    print(f" - {book.title}")

print("\n2. All books in Central Library:")
# Query 2: All books in a library
library = Library.objects.get(name="Central Library")
for book in library.books.all():
    print(f" - {book.title}")

print("\n3. Librarian for Central Library:")
# Query 3: Librarian for a library
librarian = Librarian.objects.get(library__name="Central Library")
print(f" - {librarian.name}")

