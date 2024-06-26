from django.db import models
from django.contrib.postgres.fields import ArrayField
from cloudinary_storage.storage import MediaCloudinaryStorage
import logging
import json
import uuid

logger = logging.getLogger(__name__)

def unique_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.unique_id}.{ext}"
    return f"images/{filename}"

class ImageModel(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True)
    image = models.ImageField(upload_to=unique_image_name, blank=True, null=True, storage=MediaCloudinaryStorage())
    image_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if isinstance(self.tags, str):
            try:
                self.tags = json.loads(self.tags)
            except json.JSONDecodeError:
                logger.warning("Failed to decode tags JSON string.")
        elif not isinstance(self.tags, list):
            self.tags = [self.tags] 
            
        if not self.unique_id:
            self.unique_id = uuid.uuid4()

        # Save image and update image_url
        super().save(*args, **kwargs)
        if self.image and not self.image_url:
            self.image_url = self.image.url
            super().save(update_fields=['image_url'])

    def __str__(self):
        return f"Image {self.unique_id}"
