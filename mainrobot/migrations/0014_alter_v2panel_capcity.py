# Generated by Django 5.0.4 on 2024-04-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0013_rename_panel_user_v2panel_panel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='v2panel',
            name='capcity',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
