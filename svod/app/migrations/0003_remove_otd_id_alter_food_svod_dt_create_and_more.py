# Generated by Django 4.1.7 on 2023-03-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_otd_msister_alter_otd_zav_otd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otd',
            name='id',
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='dt_create',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='dt_svood',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='otd',
            name='idotd',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]