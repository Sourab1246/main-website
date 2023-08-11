# Generated by Django 4.2.4 on 2023-08-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppning', '0007_products_original_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='original_price',
        ),
        migrations.AddField(
            model_name='products',
            name='discount_percent',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
