# Generated by Django 5.0.7 on 2024-07-18 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_rental_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='is_active',
        ),
    ]
