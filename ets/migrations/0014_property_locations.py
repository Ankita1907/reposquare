# Generated by Django 3.2.8 on 2021-11-22 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0013_property_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='locations',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
