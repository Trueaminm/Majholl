# Generated by Django 5.0.4 on 2024-04-09 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0006_alter_admin_is_admin_alter_admin_is_owner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admin',
            new_name='admins',
        ),
        migrations.AlterModelTable(
            name='admins',
            table='TeleBot_admins',
        ),
        migrations.AlterModelTable(
            name='users',
            table='TeleBot_users',
        ),
    ]
