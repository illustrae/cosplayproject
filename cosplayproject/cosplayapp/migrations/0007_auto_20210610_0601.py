# Generated by Django 2.2 on 2021-06-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayapp', '0006_auto_20210610_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='profile_pics'),
        ),
    ]
