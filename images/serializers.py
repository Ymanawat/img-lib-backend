from rest_framework import serializers
from .models import ImageModel
import json

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('unique_id', 'tags', 'image', 'image_url')
