# Generated by Django 3.1.7 on 2021-06-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0022_auto_20210623_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='solicitado',
            field=models.IntegerField(default=39, verbose_name='Solicitado '),
        ),
    ]
