from django.urls import path
from .views import UserCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]