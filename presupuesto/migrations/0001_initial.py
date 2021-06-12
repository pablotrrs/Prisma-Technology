# Generated by Django 3.1.7 on 2021-06-12 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoPresupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.CharField(choices=[('EN EVALUACION', 'En Evaluacion'), ('APROBADO', 'Aprobado'), ('RECHAZADO', 'Rechazado')], max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPresupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Monto')),
                ('cantidad_solicitada', models.IntegerField(default=0, null=True, verbose_name='Cantidad solicitada')),
            ],
            options={
                'verbose_name': 'item de venta',
                'verbose_name_plural': 'items de ventas',
            },
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')),
                ('fecha_expiracion', models.DateTimeField(verbose_name='Fecha de expiración')),
                ('responsable_inscripto', models.BooleanField(blank=True, default=False, null=True, verbose_name='Responsable Inscripto')),
                ('total', models.IntegerField(default=0, verbose_name='Total del presupuesto')),
                ('comentarios', models.CharField(blank=True, max_length=45, null=True, verbose_name='Comentarios')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='presupuesto.estadopresupuesto')),
                ('sucursal_asociada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sucursal.sucursal')),
            ],
        ),
    ]
