# Generated by Django 3.1.7 on 2021-06-16 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4, unique=True, verbose_name='Identificador')),
                ('saldo_disponible', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Saldo disponible en pesos')),
                ('saldo_disponible_dolares', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Saldo disponible en dolares')),
                ('saldo_disponible_euros', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Saldo disponible en euros')),
                ('egresos', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Egresos')),
                ('ingresos_en_pesos', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Ingresos en pesos')),
                ('ingresos_en_dolares', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Ingresos en dolares')),
                ('ingresos_en_euros', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Ingresos en euros')),
                ('saldo_inicial', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Saldo Inicial')),
                ('saldo_final', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Saldo Final')),
            ],
            options={
                'verbose_name': 'caja',
                'verbose_name_plural': 'cajas',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4, unique=True)),
                ('idCasaCentral', models.IntegerField(default=1)),
                ('calle', models.CharField(max_length=20, verbose_name='Calle')),
                ('numero', models.CharField(max_length=4, verbose_name='Numero')),
                ('localidad', models.CharField(max_length=20, null=True, verbose_name='Localidad')),
                ('provincia', models.CharField(max_length=20, null=True, verbose_name='Provincia')),
                ('cod_postal', models.CharField(max_length=4, verbose_name='Código postal')),
            ],
            options={
                'verbose_name': 'sucursal',
                'verbose_name_plural': 'sucursales',
            },
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('monto', models.CharField(max_length=40, verbose_name='Monto')),
                ('tipo', models.CharField(max_length=10, verbose_name='Tipo')),
                ('identificador', models.CharField(max_length=30, verbose_name='Identificador')),
                ('responsable', models.IntegerField(verbose_name='ID de responsable')),
                ('caja_asociada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sucursal.caja')),
            ],
            options={
                'verbose_name': 'operacion',
                'verbose_name_plural': 'operaciones',
            },
        ),
        migrations.AddField(
            model_name='caja',
            name='sucursal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sucursal.sucursal'),
        ),
    ]
