from django.urls import path
from apps.videos.views import VideoAPIView, VideoCreateAPIView, VideoViewsCreateAPIView, VideoLikesCreateAPIView, VideoDisLikesCreateAPIView

urlpatterns = [
    path('', VideoAPIView.as_view()),
    path('create/', VideoCreateAPIView.as_view()),
    path('view/', VideoViewsCreateAPIView.as_view()),
    path('like/', VideoLikesCreateAPIView.as_view()),
    path('dislike/', VideoDisLikesCreateAPIView.as_view()),
]
