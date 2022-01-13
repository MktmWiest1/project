from book import views
from django.urls import path
urlpatterns = [
    path('books/', views.book_list_view, name='books'),
    path('books/<int:id>', views.books_detail_view, name='book1'),
]