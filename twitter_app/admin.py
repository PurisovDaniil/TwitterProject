from django.contrib import admin
from .models import Category, Image

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, PostAdmin)
admin.site.register(Image)