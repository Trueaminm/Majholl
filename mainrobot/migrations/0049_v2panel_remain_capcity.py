# Generated by Django 5.0.4 on 2024-07-11 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0048_payment_setting_back_onwername'),
    ]

    operations = [
        migrations.AddField(
            model_name='v2panel',
            name='remain_capcity',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
