from rest_framework import serializers 
from apps.videos.models import Video, VideoLikes, VideoDisLikes, VideoViews
from apps.users.serializers import UserSerializer

class VideoViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoViews
        fields = '__all__'
class VideoLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLikes
        fields = '__all__'
class VideoDisLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDisLikes
        fields = '__all__'
class VideoSeilializer(serializers.ModelSerializer):
    channel = UserSerializer(many=False, read_only=True)
    video_views = VideoViewsSerializer(many=True, read_only=True)
    video_likes = VideoLikesSerializer(many=True, read_only=True)
    video_dislikes = VideoDisLikesSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = "__all__"
