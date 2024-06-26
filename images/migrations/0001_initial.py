# Generated by Django 5.0.6 on 2024-06-25 17:09

import cloudinary_storage.storage
import django.contrib.postgres.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "unique_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "tags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=50),
                        blank=True,
                        size=None,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        storage=cloudinary_storage.storage.MediaCloudinaryStorage(),
                        upload_to="images/",
                    ),
                ),
                ("image_url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
