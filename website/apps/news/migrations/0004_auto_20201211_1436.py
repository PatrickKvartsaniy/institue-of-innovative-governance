# Generated by Django 3.1.4 on 2020-12-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201207_2141'),
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
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]