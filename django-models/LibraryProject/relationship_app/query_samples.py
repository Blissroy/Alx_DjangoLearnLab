from django.db.models import Q
from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """
    Query all books by a specific author using objects.filter()
    Returns a QuerySet of Book objects
    """
    return Book.objects.filter(author__name=author_name)

def get_books_in_library(library_name):
    """
    List all books in a library
    Returns a QuerySet of Book objects
    """
    return Book.objects.filter(libraries__name=library_name)

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library
    Returns a Librarian object or None
    """
    try:
        return Librarian.objects.get(library__name=library_name)
    except Librarian.DoesNotExist:
        return None
