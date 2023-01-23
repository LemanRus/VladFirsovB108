from django.db import models

from core.models import CustomUser


def ad_image_path(instance, filename):
    user_id = instance.id
    return f'user_photos/user-{user_id}/{filename}'


class Category(models.Model):
    title = models.CharField(max_length=150, blank=False, default='Common')
    description = models.TextField(max_length=5000, blank=False, default='Uncategorized goods category')

    class Meta:
        verbose_name_plural = 'Categories'

    @classmethod
    def get_default_pk(cls):
        default_category, created = cls.objects.get_or_create(
            title='Common',
        )
        return default_category.pk

    def __str__(self):
        return f"{self.title}"

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]


class Advertisement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=5000, blank=False)
    image = models.ImageField(upload_to=ad_image_path, default='default.png')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, related_name='advertisements', default=Category.get_default_pk)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f"Ad \"{self.title}\""


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=200)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment from {} to ad #{}".format(self.author, self.ad.id)