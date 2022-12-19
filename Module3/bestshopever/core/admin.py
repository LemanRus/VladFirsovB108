from django.contrib import admin

from .models import CustomUser, Rating

admin.site.register(CustomUser)
admin.site.register(Rating)