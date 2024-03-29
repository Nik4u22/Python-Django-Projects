from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title',)
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 10
    
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'static/js/script.js')
    

admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin)
