from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # Function-based view URL pattern
    path('books/', list_books, name='book_list'),
    
    # Class-based view URL pattern
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
