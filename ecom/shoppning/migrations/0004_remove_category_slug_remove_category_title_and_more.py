# Generated by Django 4.2.4 on 2023-08-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppning', '0003_category_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='types',
            field=models.CharField(choices=[('clothing', 'clothing'), ('shoes', 'shoes'), ('innerwear', 'innerwear'), ("men's gromming", "men's gromming"), ("men's gromming", "men's gromming"), ('Kids wear', 'kids wear')], default=False, max_length=30),
        ),
    ]
