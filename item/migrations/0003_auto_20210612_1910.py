# Generated by Django 3.1.7 on 2021-06-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20210611_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mezcla',
            name='cantidad_primera_pintura',
            field=models.IntegerField(verbose_name='Cantidad de la primera pintura (En mililitros)'),
        ),
        migrations.AlterField(
            model_name='mezcla',
            name='cantidad_segunda_pintura',
            field=models.IntegerField(verbose_name='Cantidad de la segunda pintura (En mililitros)'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='solicitado',
            field=models.IntegerField(default=35, verbose_name='Solicitado '),
        ),
    ]
