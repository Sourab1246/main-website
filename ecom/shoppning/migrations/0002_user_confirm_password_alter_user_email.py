# Generated by Django 4.2.4 on 2023-08-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
