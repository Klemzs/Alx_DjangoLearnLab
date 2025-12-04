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
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    post_search,
    posts_by_tag
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
        path('post/new/', PostCreateView.as_view(), name='post_create'),
        path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
        path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

        # Comment URLs
        path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
        path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
        path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
        path('search/', post_search, name='post_search'),
        path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),

]
