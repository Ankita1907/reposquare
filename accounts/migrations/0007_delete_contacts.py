# Generated by Django 3.2.8 on 2021-12-09 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_contacts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]