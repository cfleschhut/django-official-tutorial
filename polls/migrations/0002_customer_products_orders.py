# Generated by Django 4.1.3 on 2022-11-16 10:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("firstName", models.CharField(max_length=100)),
                ("lastName", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=100)),
                ("plz", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Products",
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
                ("product", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=100)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
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
                ("orderDate", models.DateTimeField(default=datetime.datetime.now)),
                ("amount", models.IntegerField()),
                (
                    "articleOrdered",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.products"
                    ),
                ),
                (
                    "customerID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.customer"
                    ),
                ),
            ],
        ),
    ]