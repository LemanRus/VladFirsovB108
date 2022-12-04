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
    # rate = models.ManyToManyField(CustomUser, through='Rating')

    @property
    def rating_calc(self):
        return Advertisement.objects.aggregate(calculated_rating=models.Avg('rating__rating_value')).get('calculated_rating')

    def __str__(self):
        print(self.rating_calc)
        return f"Ad from {self.author} with rating {self.rating_calc}"


class Category(models.Model):
    pass


class Stars(models.IntegerChoices):
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    rating_value = models.IntegerField(default=Stars.FIVE, choices=Stars.choices)

    def __str__(self):
        return f'User {self.user} rated ad \"{self.advertisement}\" with {self.rating_value} stars'
