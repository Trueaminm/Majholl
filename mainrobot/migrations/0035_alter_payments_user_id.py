# Generated by Django 5.0.4 on 2024-06-14 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0034_alter_payments_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mainrobot.users', to_field='user_id'),
        ),
    ]
