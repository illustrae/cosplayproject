# Generated by Django 2.2 on 2021-06-11 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayapp', '0015_auto_20210611_0414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='wallPost',
            new_name='wall_message',
        ),
    ]