from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('book/',BookView.as_view(),name='book'),
    path('purchase/',PurchaseView.as_view(),name='purchase'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]