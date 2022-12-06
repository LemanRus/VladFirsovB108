# Generated by Django 4.1.3 on 2022-12-06 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_advertisement_category_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='categories', to='ads.category'),
        ),
    ]
