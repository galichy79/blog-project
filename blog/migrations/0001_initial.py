# Generated by Django 4.2.1 on 2023-06-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=300)),
                ("date", models.DateTimeField()),
                ("text", models.CharField()),
                ("image", models.ImageField(upload_to="event_images/")),
            ],
        ),
    ]
