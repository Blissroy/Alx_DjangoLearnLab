from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 
                 'isbn', 'page_count', 'cover_url', 'language']
        read_only_fields = ['id']
