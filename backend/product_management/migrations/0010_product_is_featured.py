# Generated by Django 3.2.8 on 2021-10-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0009_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
