# Generated by Django 5.0.4 on 2024-05-04 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainrobot', '0022_rename_capcity_v2panel_all_capcity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='v2panel',
            old_name='soled_capcity',
            new_name='sold_capcity',
        ),
    ]
