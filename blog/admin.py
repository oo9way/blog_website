from django.contrib import admin
from blog.models import Post, Category, Resume, Message
from django.utils.safestring import mark_safe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "get_body_preview")
    
    def get_body_preview(self, obj):
        return mark_safe(obj.body)
    

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "phone")