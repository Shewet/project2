# Generated by Django 3.0.2 on 2020-10-12 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20201010_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 10, 12, 9, 42, 57, 825643)),
        ),
    ]
