```python
from bookshelf.models import Book

try:
    book = Book.objects.create(
        title="1984",
        author="George Orwell",
        publication_year=1949
    )
    print(f"Successfully created: {book}")
except Exception as e:
    print(f"Error creating book: {str(e)}")
