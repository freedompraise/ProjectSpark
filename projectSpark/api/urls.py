from django.urls import path
from .views import UserRegistrationView, UserAuthenticationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('auth/', UserAuthenticationView.as_view(), name='user-auth'),
    # path('token/', UserAuthenticationView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
