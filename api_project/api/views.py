from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer  # Fixed import statement
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API endpoint that allows viewing all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    Provides all CRUD operations:
    - List (GET /books_all/)
    - Create (POST /books_all/)
    - Retrieve (GET /books_all/<id>/)
    - Update (PUT /books_all/<id>/)
    - Partial Update (PATCH /books_all/<id>/)
    - Destroy (DELETE /books_all/<id>/)
    """
    queryset = Book.objects.all().order_by('-published_date')
    serializer_class = BookSerializer
    filterset_fields = ['author', 'language']
    search_fields = ['title', 'author']
