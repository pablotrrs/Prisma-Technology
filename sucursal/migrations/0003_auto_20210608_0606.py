# Generated by Django 3.1.7 on 2021-06-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0002_auto_20210608_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacion',
            name='monto',
            field=models.CharField(max_length=40, verbose_name='Monto'),
        ),
    ]
