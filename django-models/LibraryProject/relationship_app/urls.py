from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),
<<<<<<< HEAD
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
=======
    path('LoginView.as_view(template_name='login'),
    path('LogoutView.as_view(template_name='logout'),
    path('books/add/', views.add_book, name='add_book\'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book\'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
>>>>>>> a70b1a89dc24e2e630bdc0f3c8b2c7fe4df59436
]
