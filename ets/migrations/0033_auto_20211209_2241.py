# Generated by Django 3.2.8 on 2021-12-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ets', '0032_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='Puja_room',
        ),
        migrations.RemoveField(
            model_name='property',
            name='age',
        ),
        migrations.RemoveField(
            model_name='property',
            name='balconies',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bathroom',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bedroom',
        ),
        migrations.RemoveField(
            model_name='property',
            name='booking_amount',
        ),
        migrations.RemoveField(
            model_name='property',
            name='flat_size',
        ),
        migrations.RemoveField(
            model_name='property',
            name='materials_used',
        ),
        migrations.AddField(
            model_name='property',
            name='configuration',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='property',
            name='desc',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='property',
            name='furnished',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='highlights',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='lift',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AddField(
            model_name='property',
            name='locality_recom',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='property',
            name='tower',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
