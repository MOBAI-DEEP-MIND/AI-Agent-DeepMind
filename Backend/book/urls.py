from django.urls import path
from .views import BookView,PurchaseView, SearchBookView, BookDetailView, AuthorView, CategoryView, PurchaseAgentView

urlpatterns = [
    path('books/',BookView.as_view(),name='book'),
    path('authors/',AuthorView.as_view(),name='author'),
    path('categories/',CategoryView.as_view(),name='category'),
    path('purchase/',PurchaseView.as_view(),name='purchase'),
    path('search/',SearchBookView.as_view(),name='search'),
    path('books/<int:pk>/',BookDetailView.as_view(),name='book'),
    path('purchase-agent/',PurchaseAgentView.as_view(),name='purchase-agent'),
]


