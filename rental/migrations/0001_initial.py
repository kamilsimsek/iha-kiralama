# Generated by Django 5.0.7 on 2024-07-16 03:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('DJI', 'DJI'), ('Parrot', 'Parrot'), ('Yuneec', 'Yuneec'), ('Autel', 'Autel')], max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('category', models.CharField(choices=[('Consumer', 'Consumer'), ('Professional', 'Professional'), ('Racing', 'Racing')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.drone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]