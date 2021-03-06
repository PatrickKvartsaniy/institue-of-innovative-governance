# Generated by Django 3.1.4 on 2021-03-22 16:01

from django.db import migrations, models
import website.apps.news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20201213_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[website.apps.news.models.validate_title]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_ua',
            field=models.CharField(max_length=100, validators=[website.apps.news.models.validate_title], verbose_name='Title in ukrainian'),
        ),
    ]
