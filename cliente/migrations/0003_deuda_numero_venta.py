# Generated by Django 3.1.7 on 2021-06-08 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20210607_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='deuda',
            name='numero_venta',
            field=models.BigIntegerField(default=0, verbose_name='Número de venta'),
            preserve_default=False,
        ),
    ]
