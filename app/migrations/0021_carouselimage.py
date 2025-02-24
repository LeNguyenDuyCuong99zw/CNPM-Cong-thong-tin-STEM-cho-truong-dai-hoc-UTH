# Generated by Django 5.1.5 on 2025-02-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0020_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarouselImage",
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
                ("image", models.ImageField(upload_to="carousel_images/")),
                ("alt_text", models.CharField(max_length=255)),
            ],
        ),
    ]
