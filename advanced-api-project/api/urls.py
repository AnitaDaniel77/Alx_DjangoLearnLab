ofrom django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

# URL patterns for Book API views
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),              # GET all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # GET one book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),   # POST new book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'), # PUT/PATCH book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'), # DELETE book
]

