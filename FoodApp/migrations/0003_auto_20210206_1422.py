# Generated by Django 3.0.4 on 2021-02-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_auto_20210206_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='rate',
            field=models.SmallIntegerField(choices=[('Poor', 'Poor'), ('Average', 'Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], default=1),
        ),
    ]
