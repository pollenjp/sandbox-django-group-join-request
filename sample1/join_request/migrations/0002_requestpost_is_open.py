# Generated by Django 4.0.1 on 2022-01-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestpost',
            name='is_open',
            field=models.BooleanField(default=True, verbose_name='Open'),
        ),
    ]
