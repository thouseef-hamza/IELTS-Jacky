# Generated by Django 5.0.1 on 2024-01-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_has_offer_alter_product_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
