# Generated by Django 4.2.17 on 2025-01-03 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='SettingGroup',
        ),
        migrations.AlterModelOptions(
            name='amenity',
            options={'default_related_name': 'amenities', 'ordering': ['title'], 'verbose_name_plural': 'amenities'},
        ),
        migrations.AlterModelOptions(
            name='enquiry',
            options={'default_permissions': ['view', 'change', 'delete'], 'verbose_name_plural': 'enquiries'},
        ),
        migrations.AlterModelOptions(
            name='settinggroup',
            options={'default_related_name': 'setting_group'},
        ),
        migrations.AlterModelTable(
            name='settinggroup',
            table='setting_groups',
        ),
    ]
