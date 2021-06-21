# Generated by Django 3.1.7 on 2021-06-21 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_estadoproveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='proveedor.estadoproveedor'),
            preserve_default=False,
        ),
    ]
