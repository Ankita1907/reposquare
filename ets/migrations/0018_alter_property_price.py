# Generated by Django 3.2.8 on 2021-11-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0017_property_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
