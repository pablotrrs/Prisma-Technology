# Generated by Django 3.1.7 on 2021-06-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0029_auto_20210623_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='solicitado',
            field=models.IntegerField(default=37, verbose_name='Solicitado '),
        ),
    ]
