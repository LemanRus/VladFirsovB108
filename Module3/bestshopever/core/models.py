from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from phone_field import PhoneField


def user_profile_photo_path(instance, filename):
    user_id = instance.id
    return f'user_photos/user-{user_id}/{filename}'


class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=user_profile_photo_path)
    telephone = PhoneField(blank=True)
    email = models.EmailField("email address", blank=False)
    secret_question = models.CharField(blank=False, max_length=150, default='Name of your first pet')
    secret_answer = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse('core:profile', kwargs={'user_id': self.pk})

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
    rating_value = models.IntegerField(default=Stars.FIVE, choices=Stars.choices)

    def __str__(self):
        return f'User {self.user_who_rate} rated user \"{self.user_rated}\" with {self.rating_value} stars'