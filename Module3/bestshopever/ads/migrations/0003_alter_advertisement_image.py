# Generated by Django 4.1.3 on 2023-01-14 19:20

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='default.png', upload_to=ads.models.ad_image_path),
        ),
    ]
