# Generated by Django 3.1.7 on 2021-05-16 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True, verbose_name='Estado del empleado')),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50, unique=True, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Rols',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='Correo Electrónico')),
                ('cuit', models.CharField(max_length=11, unique=True, verbose_name='Cuit')),
                ('nombre', models.CharField(max_length=16, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=16, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=13, unique=True, verbose_name='Telefono')),
                ('calle', models.CharField(blank=True, max_length=20, null=True, verbose_name='Calle')),
                ('numero', models.CharField(blank=True, max_length=4, null=True, verbose_name='Numero')),
                ('localidad', models.CharField(blank=True, max_length=20, null=True, verbose_name='Localidad')),
                ('provincia', models.CharField(blank=True, max_length=20, null=True, verbose_name='Provincia')),
                ('cod_postal', models.CharField(blank=True, max_length=4, null=True, verbose_name='Código postal')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.estado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.rol')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
