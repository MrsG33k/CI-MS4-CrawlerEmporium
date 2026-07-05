from django.contrib import admin
from .models import BlogPost, BlogComment


class BlogCommentInline(admin.TabularInline):
    """ Allows admins to view and moderate comments directly inside the blog """
    model = BlogComment
    extra = 0
    readonly_fields = ('user', 'message', 'created_at')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_at')
    search_fields = ('title', 'content')
    # auto-populates the blog URL
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'author')
    inlines = [BlogCommentInline]