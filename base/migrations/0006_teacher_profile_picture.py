# Generated by Django 5.0.1 on 2024-01-26 03:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="profile_picture",
            field=models.ImageField(null=True, upload_to="teachers/"),
        ),
    ]
