# Generated by Django 3.1.3 on 2021-01-24 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0005_auto_20210124_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='name',
            new_name='tt_name',
        ),
    ]