# Generated by Django 3.1.7 on 2021-06-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_auto_20210607_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='codigo_de_barras',
            field=models.BigIntegerField(default=8499596833554, unique=True, verbose_name='Código de barras'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='solicitado',
            field=models.IntegerField(default=62, verbose_name='Solicitado '),
        ),
        migrations.AlterField(
            model_name='pinturanueva',
            name='codigo_de_barras',
            field=models.BigIntegerField(default=1214078242435, unique=True, verbose_name='Código de barras'),
        ),
        migrations.AlterField(
            model_name='pinturausada',
            name='codigo_de_barras',
            field=models.BigIntegerField(default=5800479648649, unique=True, verbose_name='Código de barras'),
        ),
    ]
