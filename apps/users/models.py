from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_image/'
    )
    USER_STATUS = (
        ('usual', 'usual'),
        ('pro', 'pro'),
        ('admin', 'admin'),
    )
    email = models.EmailField(
        max_length=55,
        blank=True,
        null=True
    )
    user_status = models.CharField(
        choices= USER_STATUS,
        max_length=25
    )