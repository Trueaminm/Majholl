# Generated by Django 5.0.4 on 2024-04-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0005_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='is_admin',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='admin',
            name='is_owner',
            field=models.BooleanField(default=0),
        ),
    ]
