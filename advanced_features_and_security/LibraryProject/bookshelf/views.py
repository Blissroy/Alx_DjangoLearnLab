from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

def form_example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process data
            return redirect('success_url')
    else:
        form = ExampleForm()
    return render(request, 'form_example.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # code to create a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    # code to edit a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    # code to delete a book
    pass
# Create your views here.
