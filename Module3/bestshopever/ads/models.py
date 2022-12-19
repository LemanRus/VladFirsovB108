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
        created_default = Category.objects.create().id
        created_default.save()
        return created_default


class Advertisement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=5000, blank=False)
    image = models.ImageField(upload_to=ad_image_path)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    # rate = models.ManyToManyField(CustomUser, through='Rating')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, related_name='advertisements', default=default_category())

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f"Ad \"{self.title}\" from {self.author} with rating {self.author.rating_calc}"


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=200)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment from {} to ad #{}".format(self.author, self.ad.id)