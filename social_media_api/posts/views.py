from rest_framework import viewsets, permissions, filters, generics,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from django.contrib.contenttypes.models import ContentType


class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(content__icontains=search)
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
        
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )
        
        return Response({'detail': 'Post liked'})
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({'detail': 'Not liked'}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()
        return Response({'detail': 'Post unliked'})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination
    
    def get_queryset(self):
        user = self.request.user
        # Get users that the current user is following
        following_users = user.following.all()
        # Get posts from followed users, ordered by creation date (most recent first)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
