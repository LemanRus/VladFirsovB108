from django.db import models

from bestclassified.models import CustomUser


def ad_image_path(instance, filename):
    user_id = instance.id
    return f'user_photos/user-{user_id}/{filename}'


class Category(models.Model):
    title = models.CharField(max_length=150, blank=False, default='Common')

    def __str__(self):
        return f"{self.title} with ID{self.id}"


def default_category():
    try:
        existing_default_category = Category.objects.get(title='Common').id
    except:
        existing_default_category = None
    if existing_default_category:
        return existing_default_category
    else:
        return Category.objects.create().id


class Advertisement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=5000, blank=False)
    image = models.ImageField(upload_to=ad_image_path)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    # rate = models.ManyToManyField(CustomUser, through='Rating')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, related_name='categories', default=default_category())

    @property
    def rating_calc(self):
        return Advertisement.objects.filter(rating__advertisement=self).aggregate(calculated_rating=models.Avg('rating__rating_value')).get('calculated_rating')

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f"Ad \"{self.title}\" from {self.author} with rating {self.rating_calc}"


class Stars(models.IntegerChoices):
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rating')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='rating')
    rating_value = models.IntegerField(default=Stars.FIVE, choices=Stars.choices)

    def __str__(self):
        return f'User {self.user} rated ad \"{self.advertisement}\" with {self.rating_value} stars'
