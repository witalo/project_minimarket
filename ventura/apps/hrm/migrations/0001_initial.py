# Generated by Django 3.0.5 on 2021-02-07 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsidiary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('serial', models.CharField(blank=True, max_length=4, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('ruc', models.CharField(max_length=11)),
                ('business_name', models.CharField(blank=True, max_length=45, null=True, verbose_name='Razón social')),
                ('legal_representative_name', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_representative_dni', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Filial',
                'verbose_name_plural': 'Filiales',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document_number', models.CharField(blank=True, max_length=15, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('paternal_last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('maternal_last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('names', models.CharField(blank=True, max_length=40, null=True)),
                ('gender', models.CharField(choices=[('1', 'Masculino'), ('2', 'Femenino')], default='1', max_length=1, verbose_name='Sexo')),
                ('telephone_number', models.CharField(blank=True, max_length=9, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('photo', models.ImageField(blank=True, default='employee/employee0.jpg', upload_to='employee/')),
                ('occupation', models.CharField(choices=[('1', 'Administrador'), ('2', 'Gerente General'), ('3', 'Gerente de Recursos Humanos'), ('4', 'Gerente de Operacione'), ('5', 'Gerente de Logística'), ('6', 'Gerente Financiero'), ('7', 'Gerente Comercial'), ('8', 'Gerente de Marketing'), ('9', 'Cajero'), ('10', 'Mesero '), ('11', 'Sin Asignar')], default='11', max_length=50, verbose_name='Ocupacion')),
                ('is_state', models.BooleanField(default=False, verbose_name='Estado')),
                ('subsidiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm.Subsidiary')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
