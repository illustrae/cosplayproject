# Generated by Django 2.2 on 2021-06-11 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayapp', '0016_auto_20210611_0416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_likes',
        ),
    ]
