# Generated by Django 5.0.4 on 2024-07-06 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0047_payment_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_setting',
            name='back_onwername',
            field=models.CharField(blank=True, max_length=124, null=True),
        ),
    ]
