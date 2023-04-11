from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255  
    )
    logo = models.ImageField(
        upload_to= 'logo/'
    )