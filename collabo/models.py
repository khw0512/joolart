from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


def image_upload_path(instance, filename):
    return f'{instance}/{filename}'


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    content = RichTextUploadingField('CONTENT')
    main_img = models.ImageField(upload_to=image_upload_path)
    img_artist = models.CharField(max_length=30)
    bgmusic = models.CharField(max_length=50)
    music_artist = models.CharField(max_length=30)
    desc = models.TextField()
    pay = models.BooleanField(default=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
