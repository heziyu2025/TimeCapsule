# Generated by Django 4.2.9 on 2024-01-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capsule',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]