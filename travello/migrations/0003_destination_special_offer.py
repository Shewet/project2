# Generated by Django 3.0.2 on 2020-10-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20201012_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='special_offer',
            field=models.BooleanField(default=False),
        ),
    ]
