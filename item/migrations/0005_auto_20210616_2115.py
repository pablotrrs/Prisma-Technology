# Generated by Django 3.1.7 on 2021-06-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20210616_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='solicitado',
            field=models.IntegerField(default=56, verbose_name='Solicitado '),
        ),
    ]
