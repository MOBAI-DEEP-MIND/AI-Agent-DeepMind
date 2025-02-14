from django.urls import path
from .views import BookView,PurchaseView, SearchBookView, BookDetailView, AuthorView, CategoryView

urlpatterns = [
    path('book/',BookView.as_view(),name='book'),
    path('book/<int:pk>/',BookView.as_view(),name='book'),
    path('books/',BookDetailView.as_view(),name='books'),
    path('books/<int:pk>/',BookDetailView.as_view(),name='books'),
    path('authors/',AuthorView.as_view(),name='author'),
    path('authors/<int:pk>/',AuthorView.as_view(),name='author'),
    path('categories/',CategoryView.as_view(),name='category'),
    path('categories/<int:pk>',CategoryView.as_view(),name='category'),
    path('purchase/',PurchaseView.as_view(),name='purchase'),
    path('search/',SearchBookView.as_view(),name='search'),
]


