# Generated by Django 3.2.8 on 2021-12-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0026_property_landmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='overlook',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
