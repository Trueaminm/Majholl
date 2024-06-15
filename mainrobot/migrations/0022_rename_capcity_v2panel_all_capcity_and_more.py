# Generated by Django 5.0.4 on 2024-05-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0021_alter_v2panel_reality_flow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='v2panel',
            old_name='capcity',
            new_name='all_capcity',
        ),
        migrations.AddField(
            model_name='v2panel',
            name='capcity_mode',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='v2panel',
            name='panel_sale_mode',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='v2panel',
            name='send_links_mode',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='v2panel',
            name='send_qrcode_mode',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='v2panel',
            name='soled_capcity',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
