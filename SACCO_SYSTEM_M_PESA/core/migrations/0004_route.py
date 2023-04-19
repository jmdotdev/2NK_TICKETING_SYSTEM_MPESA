# Generated by Django 4.0.4 on 2022-05-22 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=200)),
                ('Destination', models.CharField(max_length=200)),
                ('Day', models.DateField()),
                ('Departure_Time', models.TimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.car')),
            ],
            options={
                'verbose_name_plural': 'Routes',
            },
        ),
    ]