from django.contrib import admin
from .models import ImageModel

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'tags', 'image_url')
    readonly_fields = ('image_url',)