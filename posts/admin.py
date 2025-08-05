from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('vehicle', 'slug', 'status')
    list_filter = ('status', 'created_on', 'user', 'approved')
    prepopulated_fields = {'slug': ('vehicle',)}
    summernote_fields = ('content',)

    def make_published(self, request, queryset):
        queryset.update(status=1)
    make_published.short_description = "mark selected posts as published"
