# Generated by Django 4.1.7 on 2023-03-08 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_food_svod_diet_vkb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food_svod',
            name='fio_ms',
        ),
    ]
