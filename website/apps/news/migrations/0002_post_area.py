# Generated by Django 3.1.4 on 2020-12-07 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0004_auto_20201207_1044'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='area',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='areas.area'),
        ),
    ]
