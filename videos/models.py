from django.db import models
from .validators import file_size
# Create your models here.

class Video(models.Model):
    Caption = models.CharField(max_length=100)
    Video = models.FileField(upload_to='media/video/%y', validators=[file_size])

    def __str__(self):
        return self.Caption
    

