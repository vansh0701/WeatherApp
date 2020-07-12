# Generated by Django 3.0.6 on 2020-06-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('base', models.CharField(max_length=100)),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
            ],
        ),
    ]
