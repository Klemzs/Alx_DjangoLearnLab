# To create 

from bookshelf.models import Book

book = Book.objects.create(
            title = "1984",
            author = "George Orwell",
            publication_year = 1949
            )

print(book)

# Expected Output

# Output: 1


# To Retrieve

from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Expected Output:  Title: 1984, Author: George Orwell, Year: 1949


# TO UPDATE

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")

# Expected Output:   Updated title: Nineteen Eighty-Four


# TO DELETE

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
all_books = Book.objects.all()
print(f"Books in database: {all_books.count()}")

# Expected Output:   Books in database: 0
