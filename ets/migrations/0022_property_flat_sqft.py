# Generated by Django 3.2.8 on 2021-11-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0021_alter_property_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='flat_sqft',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
