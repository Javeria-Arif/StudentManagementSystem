# Generated by Django 3.1.3 on 2021-01-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0016_auto_20210125_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcomplaint',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
