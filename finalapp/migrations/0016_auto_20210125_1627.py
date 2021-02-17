# Generated by Django 3.1.3 on 2021-01-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0015_auto_20210125_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcomplaint',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='studentcomplaint',
            name='rating',
            field=models.CharField(choices=[('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], default='none', max_length=100, null=True),
        ),
    ]
