from django.urls import path
from . import views
urlpatterns = [

    path('book/', views.BookListViews.as_view(), name='book_all'),
    path('book/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:id>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:id>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('add-book/', views.BookCreateView.as_view(), name='add_book'),
]
