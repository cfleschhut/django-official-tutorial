# Generated by Django 4.1.3 on 2022-11-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_customer_products_orders"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="image_src",
            field=models.CharField(default="", max_length=200),
        ),
    ]