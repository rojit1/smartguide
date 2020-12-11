# Generated by Django 3.1.4 on 2020-12-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.CharField(blank=True, max_length=100)),
                ('lng', models.CharField(blank=True, max_length=100)),
                ('is_world_herritage', models.BooleanField(default=False)),
                ('is_city_area', models.BooleanField(default=False)),
                ('major_district', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.ManyToManyField(to='places.Place')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
