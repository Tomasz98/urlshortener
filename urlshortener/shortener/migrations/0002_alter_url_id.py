# Generated by Django 4.2.4 on 2023-08-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]