# Generated by Django 4.1.7 on 2023-03-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_svod',
            name='diet_age_11_18',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food_svod',
            name='diet_age_1_3',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food_svod',
            name='diet_age_3_7',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food_svod',
            name='diet_age_7_11',
            field=models.SmallIntegerField(default=0),
        ),
    ]
