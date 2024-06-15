# Generated by Django 5.0.4 on 2024-04-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0017_v2panel_panel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='v2panel',
            name='panel_id',
        ),
        migrations.AddField(
            model_name='v2panel',
            name='panel_id_str',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
