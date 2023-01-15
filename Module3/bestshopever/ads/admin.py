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
        (None, {'fields': ['author', 'status']}),
        ('Advertisement content', {'fields': ['title', 'description', 'image', 'category',]}),
        ('Date information', {'fields': ['date_pub', 'date_edit']}),
    ]
    readonly_fields = ['date_pub', 'date_edit']
    inlines = [CommentInline]
    list_display = ['__str__', 'description', 'author', 'category', 'status', 'date_pub']
    list_display_links = ['__str__', 'description']
    list_editable = ['category', 'status']
    sortable_by = ['date_pub']
    list_filter = ['category', 'date_pub']
    search_fields = ['author__username', 'author__first_name', 'author__last_name', 'title', 'category']
    actions = ['make_public']

    def make_public(self, request, queryset):
        queryset.update(status='p')

admin.site.register(Advertisement, AdvertisementAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'description']}),
    ]
    readonly_fields = []
    inlines = [AdvertisementInline]
    list_display = ['title', 'description',]
    list_display_links = ['title']
    list_editable = ['description']
    sortable_by = ['title']
    list_filter = ['title']
    search_fields = ['title', 'description']


admin.site.register(Category, CategoryAdmin)
