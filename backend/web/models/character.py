import uuid
from time import localtime

from django.db import models

from web.models.user import UserProfile  # noqa: F401


def photo_photo_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'character/photo/{instance.author.user_id}/{filename}'
    
def background_photo_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'character/background/{instance.author.user_id}/{filename}'

class Character(models.Model):
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to=photo_photo_to)
    profile = models.TextField(max_length=255)
    background = models.ImageField(upload_to=background_photo_to)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author.user.username} - {self.author.user_id} - {localtime(self.create_time.timestamp())}'
    
