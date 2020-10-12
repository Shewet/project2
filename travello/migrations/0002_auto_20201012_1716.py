# Generated by Django 3.0.2 on 2020-10-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destination',
            options={'verbose_name': 'Destination', 'verbose_name_plural': 'Destinations'},
        ),
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]