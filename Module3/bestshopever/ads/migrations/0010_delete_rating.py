# Generated by Django 4.1.3 on 2022-12-08 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_alter_advertisement_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]