# Generated by Django 4.1.7 on 2023-03-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_food_svod_diet_age_11_18_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_svod',
            name='dop',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]