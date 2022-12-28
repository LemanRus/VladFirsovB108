# Generated by Django 4.1.3 on 2022-12-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='secret_answer',
            field=models.CharField(default='Fido', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='secret_question',
            field=models.CharField(default='Name of your first pet', max_length=150),
        ),
    ]