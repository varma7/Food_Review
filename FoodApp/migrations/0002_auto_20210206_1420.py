# Generated by Django 3.0.4 on 2021-02-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodmodel',
            name='diet',
            field=models.SmallIntegerField(choices=[(1, 'BreakFast'), (2, 'Lunch'), (3, 'Snacks'), (4, 'Dinner')]),
        ),
    ]
