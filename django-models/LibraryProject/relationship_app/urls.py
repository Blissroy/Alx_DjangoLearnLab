from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),
    path('LoginView.as_view(template_name='login'),
    path('LogoutView.as_view(template_name='logout'),
]
