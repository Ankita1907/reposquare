# Generated by Django 3.2.8 on 2021-11-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0014_property_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='locations',
            field=models.CharField(default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,", max_length=1000),
        ),
    ]