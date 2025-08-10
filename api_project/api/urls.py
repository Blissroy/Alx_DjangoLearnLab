from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book')

urlpatterns = [
    # Original path for BookList view
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include router-generated URLs
    path('', include(router.urls)),
]
