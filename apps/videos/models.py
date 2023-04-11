from django.db import models
from apps.users.models import User

class Video(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(
        max_length=2000
    )
    poster = models.FileField(
        upload_to='poster/'
    )
    video_file = models.FileField(
        upload_to='video_file/'
    )
    channel = models.ForeignKey(    
        User,
        related_name='user_video',
        on_delete=models.CASCADE
    )
    slug = models.CharField(
        max_length=255,
        unique=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

class VideoLikes(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='user_likes',
        on_delete=models.CASCADE
    )
    to_video = models.ForeignKey(
        Video,
        related_name='video_likes',
        on_delete=models.CASCADE
    )
class VideoDisLikes(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='user_dislikes',
        on_delete=models.CASCADE
    )
    to_video = models.ForeignKey(
        Video,
        related_name='video_dislikes',
        on_delete=models.CASCADE
    )
class VideoViews(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='user_views',
        on_delete=models.CASCADE
    )
    to_video = models.ForeignKey(
        Video,
        related_name='video_views',
        on_delete=models.CASCADE
    )