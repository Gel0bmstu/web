# Generated by Django 2.1.3 on 2018-11-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ask_Gel0', '0005_auto_20181105_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
