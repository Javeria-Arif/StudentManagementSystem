# Generated by Django 3.1.3 on 2021-01-24 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0010_studentattendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentattendance',
            old_name='studentid',
            new_name='sid',
        ),
    ]
