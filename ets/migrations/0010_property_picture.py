# Generated by Django 3.2.8 on 2021-11-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0009_auto_20211120_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='picture',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
