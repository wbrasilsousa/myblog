from django.contrib import admin
from blog.models import Category, Comment, Post
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)