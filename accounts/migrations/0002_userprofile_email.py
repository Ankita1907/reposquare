# Generated by Django 3.2.8 on 2021-12-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='ank@gmail.com', max_length=254),
        ),
    ]
