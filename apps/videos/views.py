from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.videos.models import Video, VideoViews, VideoLikes, VideoDisLikes
from apps.videos.serializers import VideoSeilializer, VideoViewsSerializer, VideoLikesSerializer, \
    VideoDisLikesSerializer


class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSeilializer
    permission_classes = [AllowAny, ]


class VideoCreateAPIView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSeilializer
    permission_classes = [AllowAny, ]


class VideoViewsCreateAPIView(generics.CreateAPIView):
    queryset = VideoViews.objects.all()
    serializer_class = VideoViewsSerializer
    permission_classes = [AllowAny, ]


class VideoLikesCreateAPIView(generics.CreateAPIView):
    queryset = VideoLikes.objects.all()
    serializer_class = VideoLikesSerializer
    permission_classes = [AllowAny, ]


class VideoDisLikesCreateAPIView(generics.CreateAPIView):
    queryset = VideoDisLikes.objects.all()
    serializer_class = VideoDisLikesSerializer
    permission_classes = [AllowAny, ]
