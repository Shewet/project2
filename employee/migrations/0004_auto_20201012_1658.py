# Generated by Django 3.0.2 on 2020-10-12 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20201012_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2020, 10, 12, 16, 58, 47, 903887)),
        ),
    ]
