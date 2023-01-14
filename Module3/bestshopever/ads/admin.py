from django.contrib import admin

from .models import Advertisement, Category, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'text', 'date_pub']
    readonly_fields = ['date_pub']
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class AdvertisementInline(admin.TabularInline):
    model = Advertisement
    fieldsets = [
        ('Advertisement content', {'fields': ['title', 'description', 'image', 'category', ]}),
    ]
    extra = 0


class AdvertisementAdmin(admin.ModelAdmin):
    fieldsets =[
        (None, {'fields': ['author', ]}),
        ('Advertisement content', {'fields': ['title', 'description', 'image', 'category',]}),
        ('Date information', {'fields': ['date_pub', 'date_edit']}),
    ]
    readonly_fields = ['date_pub', 'date_edit']
    inlines = [CommentInline]
    list_display = ['__str__', 'description', 'category', 'date_pub']
    list_editable = ['category']


admin.site.register(Advertisement, AdvertisementAdmin)

admin.site.register(Category)
