from django.urls import path
from .views import (
    CustomLoginView, 
    CustomLogoutView, 
    register, 
    profile, 
    profile_update, 
    change_password,
    home,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
        # Authenticate URLs 
        path('', home, name='home'),
        path('login/', CustomLoginView.as_view(), name = 'login'),
        path('logout/', CustomLogoutView.as_view(), name = 'logout'),
        path('register/', register, name = 'register'),
        path('profile/', profile, name = 'profile'),

        # Add Profile management URLs
        path('profile/update/', profile_update, name = 'profile_update'),
        path('profile/change-password/', change_password, name = 'change_password'),

        # CRUD URLs for blog posts
        path('posts/', PostListView.as_view(), name='post_list'),
        path('posts/new/', PostCreateView.as_view(), name='post_create'),
        path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
        path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
