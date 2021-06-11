# Generated by Django 2.2 on 2021-06-11 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayapp', '0014_auto_20210610_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='postUser',
            new_name='poster',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='postUser',
            new_name='poster',
        ),
        migrations.AlterField(
            model_name='message',
            name='message_likes',
            field=models.ManyToManyField(related_name='liked_posts', to='cosplayapp.User'),
        ),
    ]
