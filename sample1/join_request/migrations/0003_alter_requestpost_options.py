# Generated by Django 4.0.1 on 2022-01-26 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join_request', '0002_requestpost_is_open'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestpost',
            options={'permissions': [('view_request_post_all', 'Can view all request posts'), ('approve_request_post', 'Can approve request post')]},
        ),
    ]