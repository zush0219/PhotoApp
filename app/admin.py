from django.contrib import admin
from .models import Photo, Category, Icon, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class IconAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Icon, IconAdmin)
admin.site.register(Comment, CommentAdmin)
