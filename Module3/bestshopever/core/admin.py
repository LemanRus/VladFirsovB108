from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Rating
from ads.admin import AdvertisementInline


class RatingInline(admin.TabularInline):
    model = Rating
    fk_name = 'user_rated'
    fields = ['user_who_rate', 'rating_value']
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "photo",
            "telephone")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        ("Password change information", {
            "fields": (
                "secret_question",
                "secret_answer"
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    readonly_fields = ['date_joined', 'last_login']
    inlines = [AdvertisementInline, RatingInline]
    actions = ['make_stuff']

    def make_stuff(self, request, queryset):
        queryset.update(is_staff=True)

    def dismiss_stuff(self, request, queryset):
        queryset.update(is_staff=False)


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Rating)
