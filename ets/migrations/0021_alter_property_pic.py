# Generated by Django 3.2.8 on 2021-11-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0020_alter_property_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='pic',
            field=models.ImageField(default='', upload_to='ets/images'),
        ),
    ]