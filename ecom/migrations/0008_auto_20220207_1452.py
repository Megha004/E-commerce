# Generated by Django 3.0.5 on 2022-02-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_auto_20220207_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
