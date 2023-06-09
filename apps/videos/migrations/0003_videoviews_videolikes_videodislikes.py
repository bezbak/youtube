# Generated by Django 4.1.7 on 2023-03-29 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_video_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_views', to=settings.AUTH_USER_MODEL)),
                ('to_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_views', to='videos.video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
                ('to_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_likes', to='videos.video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoDisLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_dislikes', to=settings.AUTH_USER_MODEL)),
                ('to_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_dislikes', to='videos.video')),
            ],
        ),
    ]
