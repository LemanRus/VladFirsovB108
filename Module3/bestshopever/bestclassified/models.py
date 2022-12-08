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

    @property
    def rating_calc(self):
        rating = Rating.objects.filter(user_rated=self).aggregate(calculated_rating=models.Avg('rating_value')).get('calculated_rating')
        if rating:
            return rating
        else:
            return 0


class Stars(models.IntegerChoices):
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'


class Rating(models.Model):
    user_who_rate = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rate')
    user_rated = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rated')
    # advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='rating')
    rating_value = models.IntegerField(default=Stars.FIVE, choices=Stars.choices)

    def __str__(self):
        return f'User {self.user_who_rate} rated user \"{self.user_rated}\" with {self.rating_value} stars'