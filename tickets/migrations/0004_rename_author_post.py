# Generated by Django 4.1.3 on 2022-12-04 18:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0003_alter_guest_options_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Post',
        ),
    ]
