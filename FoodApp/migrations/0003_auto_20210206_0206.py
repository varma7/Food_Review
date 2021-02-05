# Generated by Django 3.0.4 on 2021-02-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_auto_20210205_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodmodel',
            options={'ordering': ('-createdon',)},
        ),
        migrations.RenameField(
            model_name='foodmodel',
            old_name='created_date',
            new_name='createdon',
        ),
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='created_date',
            new_name='createdon',
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='diet',
            field=models.CharField(choices=[('BreakFast', 'BreakFast'), ('Lunch', 'Lunch'), ('Snacks', 'Snacks'), ('Snacks', 'Dinner')], max_length=100),
        ),
    ]