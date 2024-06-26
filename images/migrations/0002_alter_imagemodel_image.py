# Generated by Django 5.0.6 on 2024-06-26 11:43

import cloudinary_storage.storage
import images.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagemodel",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=cloudinary_storage.storage.MediaCloudinaryStorage(),
                upload_to=images.models.unique_image_name,
            ),
        ),
    ]
