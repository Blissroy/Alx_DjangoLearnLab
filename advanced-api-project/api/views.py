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
=======
 

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
    # In api/views.py
from rest_framework.response import Response
from rest_framework import status

class BookCreateView(generics.CreateAPIView):
    # ... existing code ...
    
    def create(self, request, *args, **kwargs):
        """Custom create method with enhanced response"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status': 'success',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

class BookUpdateView(generics.UpdateAPIView):
    # ... existing code ...
    
    def update(self, request, *args, **kwargs):
        """Custom update method with partial updates support"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response({
            'status': 'success',
            'data': serializer.data
        })
        from .permissions import IsOwnerOrReadOnly

class BookUpdateView(generics.UpdateAPIView):
    # ... existing code ...
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    # ... existing code ...
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
>>>>>>> 654fed327fd21993d1b397dac16b82abcb85a5d3

