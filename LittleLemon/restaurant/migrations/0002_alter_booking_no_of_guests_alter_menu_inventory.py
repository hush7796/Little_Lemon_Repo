# Generated by Django 4.2.7 on 2023-12-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]
