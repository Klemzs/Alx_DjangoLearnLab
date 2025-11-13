from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Book

# View to create new book - requires can_create permission
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Simple creation without form
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        
        if title and author and publication_year:
            Book.objects.create(
                title=title,
                author=author,
                publication_year=publication_year
            )
            messages.success(request, 'Book created successfully!')
            return redirect('book_list')
        else:
            messages.error(request, 'Please fill all fields.')
    
    return render(request, 'bookshelf/book_create.html')  # Different template

# View to edit existing book - requires can_edit permission
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        # Simple update without form
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        
        messages.success(request, 'Book updated successfully!')
        return redirect('book_detail', pk=book.pk)
    
    return render(request, 'bookshelf/book_edit.html', {'book': book})  # Different template

# Book list view - requires can_view permission
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Book detail view - requires can_view permission
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

# Book delete view - requires can_delete permission
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
