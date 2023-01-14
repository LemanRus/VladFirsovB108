from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Rating
from ads.admin import AdvertisementInline


class CustomUserAdmin(UserAdmin):
    inlines = [AdvertisementInline, ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Rating)
