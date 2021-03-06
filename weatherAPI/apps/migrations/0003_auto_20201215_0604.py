# Generated by Django 3.1.4 on 2020-12-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20201215_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='humidity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='history',
            name='maxtp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='history',
            name='mintp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='history',
            name='temp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
