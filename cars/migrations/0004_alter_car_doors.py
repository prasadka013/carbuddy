# Generated by Django 4.0 on 2022-12-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_description_alter_car_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], max_length=10),
        ),
    ]
