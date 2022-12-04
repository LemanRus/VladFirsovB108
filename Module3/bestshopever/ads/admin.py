from django.contrib import admin

from .models import Advertisement, Stars, Rating, Category

admin.site.register(Advertisement)
admin.site.register(Rating)
admin.site.register(Category)
