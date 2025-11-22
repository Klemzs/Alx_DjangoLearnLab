from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
        path('books/', BookList.as_view(), name = 'book_list'),
        path('', include(router.urls)),
        path('auth_token/', obtain_auth_token, name='auth_token'),
        ]
