from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Represents an author who writes books.
    
    Fields:
        name (CharField): The name of the author (max length 100 characters)
    """
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Book(models.Model):
    """
    Represents a book written by an author.
    
    Fields:
        title (CharField): The title of the book (max length 200 characters)
        publication_year (IntegerField): The year the book was published
        author (ForeignKey): Reference to the Author who wrote this book
                            (one-to-many relationship: one author can have many books)
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def _str_(self):
        return f"{self.title} by {self.author.name} ({self.publication_year})"
