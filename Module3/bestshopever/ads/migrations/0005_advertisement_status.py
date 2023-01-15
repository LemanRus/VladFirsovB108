# Generated by Django 4.1.3 on 2023-01-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_category_options_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
        ),
    ]
