# Generated by Django 3.1.4 on 2020-12-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='place',
        ),
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ManyToManyField(to='places.Category'),
        ),
    ]
