from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

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
 

class BookListView(generics.ListAPIView):
    """
    View to list all books (GET)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by ID (GET)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book (POST)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        """Additional actions when creating a book"""
        serializer.save()  # You could add owner=self.request.user here if needed

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book (PUT/PATCH)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book (DELETE)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
