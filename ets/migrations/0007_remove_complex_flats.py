# Generated by Django 3.2.8 on 2021-11-20 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0006_complex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complex',
            name='flats',
        ),
    ]
