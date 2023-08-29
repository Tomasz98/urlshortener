# Generated by Django 4.2.4 on 2023-08-29 15:26

from django.db import migrations, models
import shortener.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URL",
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
                ("original_url", models.URLField()),
                (
                    "short_code",
                    models.CharField(
                        default=shortener.models.generate_unique_code,
                        max_length=15,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]