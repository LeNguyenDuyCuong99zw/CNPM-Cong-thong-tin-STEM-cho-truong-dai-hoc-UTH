# Generated by Django 5.1.5 on 2025-02-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0027_customuser_email_customuser_hovaten"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webpage",
            name="category",
            field=models.CharField(
                choices=[
                    ("tin-tuc-su-kien", "Tin Tức"),
                    ("tuyen-sinh", "Tuyển Sinh"),
                    ("other", "Khác"),
                ],
                default="other",
                max_length=50,
            ),
        ),
    ]
