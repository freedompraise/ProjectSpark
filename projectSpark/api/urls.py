from django.urls import path
from .views import UserRegistrationView, UserAuthenticationView, IdeaListAPIVIEW, IdeaDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('auth/', UserAuthenticationView.as_view(), name='user-auth'),
    path('ideas/', IdeaListAPIVIEW.as_view(), name='idea-list'),
    path('ideas/<int:pk>/', IdeaDetailAPIView.as_view(), name='idea-detail'),
]
