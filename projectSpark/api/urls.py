from django.urls import path
from .views import (
    UserRegistrationView, IdeaListAPIView, 
    IdeaDetailAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, UserLoginView, 
    TagListAPIView, IdeaListByTagAPIView, IdeaRatingCreateAPIView, IdeaRatingListAPIView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('ideas/', IdeaListAPIView.as_view(), name='idea-list'),
    path('ideas/<int:pk>/', IdeaDetailAPIView.as_view(), name='idea-detail'),
    path('ideas/<int:idea_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-create'),
    path('ideas/<int:idea_id>/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('tags/',TagListAPIView.as_view(), name = 'tag-list' ),
    path('ideas/<slug:tag_slug>/',IdeaListByTagAPIView.as_view(), name = 'idea-list-by-tag'),

]
