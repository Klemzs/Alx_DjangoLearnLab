from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view URL pattern
    path('books/', list_books, name='book_list'),
    
    # Class-based view URL pattern
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
