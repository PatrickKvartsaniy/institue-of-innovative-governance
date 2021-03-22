# Generated by Django 3.1.4 on 2021-03-22 16:01

from django.db import migrations, models
import website.apps.areas.models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0005_auto_20201211_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='title',
            field=models.CharField(max_length=100, validators=[website.apps.areas.models.validate_title]),
        ),
        migrations.AlterField(
            model_name='area',
            name='title_ua',
            field=models.CharField(max_length=100, validators=[website.apps.areas.models.validate_title], verbose_name='Title in ukrainian'),
        ),
    ]