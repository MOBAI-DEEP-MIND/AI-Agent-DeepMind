from django.urls import path
from .views import CreateUserView,EditUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("edit-profile/", EditUserView.as_view(), name="edit"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]