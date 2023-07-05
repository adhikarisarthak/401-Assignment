# Generated by Django 4.2.2 on 2023-06-25 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='expiration_date',
        ),
        migrations.AddField(
            model_name='itemfridge',
            name='expiration_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
