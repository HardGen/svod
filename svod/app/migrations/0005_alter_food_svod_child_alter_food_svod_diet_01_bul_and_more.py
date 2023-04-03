# Generated by Django 4.1.7 on 2023-04-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_food_svod_dop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_svod',
            name='child',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_01_bul',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_01_kis',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_02',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_03',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_child',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_nbd',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_nkd',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_ovd',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_shd',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='diet_vdb',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='golod',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='mam',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='mam_nofood',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='priznak',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='vsego',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='wow',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='food_svod',
            name='zond',
            field=models.SmallIntegerField(default=0, null=True),
        ),
    ]
