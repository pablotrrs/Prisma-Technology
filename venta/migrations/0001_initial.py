# Generated by Django 3.1.7 on 2021-05-24 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('cliente', '0001_initial'),
        ('sucursal', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.CharField(choices=[('CANCELADO POR EL CLIENTE', 'Cancelada Por Cliente'), ('CANCELADO POR LA SUCURSAL', 'Cancelada Por Sucursal'), ('PENDIENTE DE RETIRO', 'Pendiente De Retiro'), ('EN PREPARACIÓN', 'En Preparacion'), ('LISTA', 'Lista'), ('PAGADA', 'Pagada'), ('RETIRADA', 'Retirada'), ('RECHAZADA', 'Rechazada'), ('NO RETIRADO', 'No Retirado')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha')),
                ('numero_comprobante', models.CharField(max_length=25, unique=True, verbose_name='Número de comprobrante')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total')),
                ('cliente_asociado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.cliente')),
                ('cuenta_corriente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.cuentacorriente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='venta.estadoventa')),
                ('mediodepago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.mediodepago')),
                ('sucursal_asociada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sucursal.sucursal')),
                ('vendedor_asociado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.vendedor')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='VentaLocal',
            fields=[
                ('venta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='venta.venta')),
            ],
            options={
                'verbose_name': 'venta-local',
                'verbose_name_plural': 'ventas-locales',
            },
            bases=('venta.venta',),
        ),
        migrations.CreateModel(
            name='VentaVirtual',
            fields=[
                ('venta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='venta.venta')),
                ('comentarios', models.CharField(blank=True, max_length=50, null=True, verbose_name='Comentarios')),
            ],
            options={
                'verbose_name': 'venta-virtual',
                'verbose_name_plural': 'ventas-virtuales',
            },
            bases=('venta.venta',),
        ),
        migrations.CreateModel(
            name='ItemVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Monto')),
                ('cantidad_solicitada', models.IntegerField(default=0, null=True, verbose_name='Cantidad solicitada')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
                ('sucursal_asociada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sucursal.sucursal')),
                ('venta_asociada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='venta.venta')),
            ],
            options={
                'verbose_name': 'item de venta',
                'verbose_name_plural': 'items de ventas',
            },
        ),
    ]