# Generated by Django 3.1.13 on 2021-09-29 17:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20210929_1926'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profilenew',
            new_name='Profile',
        ),
    ]