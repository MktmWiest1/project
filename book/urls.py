from django.urls import path
from . import views
urlpatterns = [
    path('book/', views.book_list_view, name='book_all'),
    path('book/<int:id>/', views.books_detail_view, name='book_detail'),
    path('add-book/', views.add_book, name='add_book'),
]
