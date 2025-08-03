from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('vehicle', 'slug', 'status')
    list_filter = ('status', 'created_on', 'user')
    prepopulated_fields = {'slug': ('vehicle',)}
    summernote_fields = ('content',)
