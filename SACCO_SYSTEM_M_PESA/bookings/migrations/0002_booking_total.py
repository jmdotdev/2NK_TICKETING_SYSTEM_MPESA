# Generated by Django 4.0.4 on 2022-06-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]