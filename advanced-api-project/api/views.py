from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerfrom django.shortcuts import render
<<<<<<< HEAD
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]   # Allow read to all, writes only to auth users

    # enable filter, search and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # simple exact-field filtering via query params (e.g. ?title=xxx&publication_year=2020)
    filterset_fields = ["title", "author", "publication_year"]

    # full-text search across these fields (e.g. ?search=potter)
    # If author is a FK, you can use 'author__name' (adjust to your model)
    search_fields = ["title", "author", "description"]

    # allow ordering via ?ordering=title or ?ordering=-publication_year
    ordering_fields = ["title", "publication_year", "author"]
    # default ordering
    ordering = ["title"]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # protect update/delete
    permission_classes = [IsAuthenticated]
    from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import BookFilter

class BookListView(generics.ListAPIView):
    """
    View to list all books with filtering, searching and ordering capabilities.
    
    Filtering:
    - /api/books/?title=Example
    - /api/books/?author__name=AuthorName
    - /api/books/?publication_year=2023
    - /api/books/?publication_year__gt=2000
    - /api/books/?publication_year__lt=2010
    
    Searching:
    - /api/books/?search=keyword (searches in title and author name)
    
    Ordering:
    - /api/books/?ordering=title (ascending)
    - /api/books/?ordering=-publication_year (descending)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
