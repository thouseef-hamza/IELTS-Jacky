# Generated by Django 5.0.1 on 2024-01-27 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0009_comment_enrollcourse_delete_feature_and_more"),
        ("products", "0005_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollcourse",
            name="course",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course_enrollment",
                to="products.product",
            ),
            preserve_default=False,
        ),
    ]
