from django.db import models

from bestclassified.models import CustomUser


def ad_image_path(instance, filename):
    user_id = instance.id
    return f'user_photos/user-{user_id}/{filename}'


class Advertisement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=5000, blank=False)
    image = models.ImageField(upload_to=ad_image_path)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
