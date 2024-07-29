from django.urls import path
from .views import search,contact,hello_pdf,export_books_csv,custom_contact,BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('search/', search, name='search'),
    path('contact/',contact, name='çontact'),
    path('custom_contact/',custom_contact, name='custom_çontact'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('export/books/', export_books_csv, name='export-books-csv'),
    path('hello-pdf/', hello_pdf, name='hello_pdf'),
]
