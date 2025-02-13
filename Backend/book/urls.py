from django.urls import path
from .views import BookView,PurchaseView

urlpatterns = [
    path('book/',BookView.as_view(),name='book'),
    path('purchase/',PurchaseView.as_view(),name='purchase'),
]


