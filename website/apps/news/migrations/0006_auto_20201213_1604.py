# Generated by Django 3.1.4 on 2020-12-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201213_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_ua',
            field=models.TextField(default='', verbose_name='Description in ukrainian'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_ua',
            field=models.CharField(default='', max_length=100, verbose_name='Title in ukrainian'),
            preserve_default=False,
        ),
    ]