from django.contrib import admin

from .models import Advertisement, Stars, Rating

admin.site.register(Advertisement)
# admin.site.register(ThingPriority)
admin.site.register(Rating)
