from django.contrib import admin
from django.http import HttpRequest
from blog.models import Post, Category, Resume, Message, Comment, Like
from django.utils.safestring import mark_safe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    readonly_fields = ("likes_count", )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "get_body_preview")
    
    def get_body_preview(self, obj):
        return mark_safe(obj.body)
    

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "phone")


@admin.register(Comment)
class CommmentAdmin(admin.ModelAdmin):
    list_display = ("id", "get_comment", "is_approved")
    ordering = ("is_approved", )

    readonly_fields = ("text", )

    def get_comment(self, obj):
        return obj.text[:100]
    
    get_comment.short_description = "Izoh"

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False
    

admin.site.register(Like)