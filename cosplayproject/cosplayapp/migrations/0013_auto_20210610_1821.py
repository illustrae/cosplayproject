# Generated by Django 2.2 on 2021-06-10 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosplayapp', '0012_auto_20210610_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosplayapp.User', unique=True),
        ),
    ]
