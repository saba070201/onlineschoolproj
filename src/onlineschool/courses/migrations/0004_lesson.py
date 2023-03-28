# Generated by Django 4.1.3 on 2023-03-27 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_module"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("video", models.FileField(upload_to="courses/videos/")),
                ("number", models.IntegerField(blank=True)),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.module"
                    ),
                ),
            ],
        ),
    ]
