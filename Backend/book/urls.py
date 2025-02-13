from django.urls import path
from .views import BookView,PurchaseView, SearchBookView, BookDetailView

urlpatterns = [
    path('books/',BookView.as_view(),name='book'),
    path('purchase/',PurchaseView.as_view(),name='purchase'),
    path('search/',SearchBookView.as_view(),name='search'),
    path('books/<int:pk>/',BookDetailView.as_view(),name='book'),
]


