from django.contrib import admin

from .models import Blog, Author


# Register your models here.

# customizer the admin form
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('whole_name', 'email')
    ordering = ('first_name', 'last_name', 'email')

    def whole_name(self, obj):
        return "{0},{1}".format(obj.first_name, obj.last_name)



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'author', 'created', 'updated', 'viewedCount')
    ordering = ('id','title', 'author', 'created', 'updated')

    fields = ('title', 'author', 'content', 'coverimg', 'readtime')
