# Generated by Django 5.0.4 on 2024-04-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0009_alter_admins_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='user_id',
            field=models.BigIntegerField(),
        ),
    ]
