from django.urls import path
from .views import BookList
["api.urls"]
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
