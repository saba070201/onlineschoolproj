# Generated by Django 4.1.5 on 2023-03-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(blank=True, max_length=100)),
                ("memo", models.TextField(blank=True)),
                ("hours", models.IntegerField(blank=True)),
                (
                    "price",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=2),
                ),
            ],
        ),
    ]
