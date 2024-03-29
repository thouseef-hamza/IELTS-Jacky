# Generated by Django 5.0.1 on 2024-01-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="accordion",
            name="profile_picture",
            field=models.ImageField(null=True, upload_to="accordion/"),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="profile_picture",
            field=models.ImageField(
                default="testimonials/user-dummy.png", upload_to="testimonials/"
            ),
        ),
        migrations.AddField(
            model_name="thumbnail",
            name="background_image",
            field=models.ImageField(default=2, upload_to="background/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="thumbnail",
            name="link_text",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
