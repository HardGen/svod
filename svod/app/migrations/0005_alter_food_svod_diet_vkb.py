# Generated by Django 4.1.7 on 2023-03-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_food_svod_diet_nbd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_svod',
            name='diet_vkb',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
