# Generated by Django 4.0.1 on 2022-01-20 17:06

# Third Party Library
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("detail", models.TextField(blank=True, verbose_name="Detail")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Creation timestamp")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="last-modified timestamp")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Post Author",
                    ),
                ),
                (
                    "request_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group", verbose_name="Request Group"
                    ),
                ),
            ],
        ),
    ]
