from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


def user_profile_photo_path(instance, filename):
    user_id = instance.id
    return f'user_photos/user-{user_id}/{filename}'


class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=user_profile_photo_path)
    telephone = PhoneField(blank=True)

    def __str__(self):
        return f"{self.username} with ID{self.id}"
