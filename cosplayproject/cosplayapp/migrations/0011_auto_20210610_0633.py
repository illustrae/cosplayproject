# Generated by Django 2.2 on 2021-06-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayapp', '0010_auto_20210610_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='profile_pics'),
        ),
    ]
