from django.contrib import admin

# Register your models here.
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','content_type', 'object_id', 'content_object', 'parent', 'content', 'timestamp')

