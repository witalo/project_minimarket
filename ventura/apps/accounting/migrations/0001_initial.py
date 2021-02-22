# Generated by Django 3.0.5 on 2021-02-07 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sale', '0001_initial'),
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre caja')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción')),
                ('type', models.CharField(choices=[('G', 'General'), ('C', 'Chica')], max_length=1, verbose_name='Tipo caja')),
                ('is_enabled', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('subsidiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrm.Subsidiary')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Caja',
                'verbose_name_plural': 'Cajas',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('I', 'INGRESO'), ('E', 'EGRESO'), ('A', 'APERTURA'), ('C', 'CIERRE')], max_length=1, verbose_name='Tipo proceso')),
                ('type_payment', models.CharField(choices=[('E', 'EFECTIVO'), ('D', 'DEPOSITO'), ('C', 'CREDITO')], max_length=1, verbose_name='Tipo proceso')),
                ('type_bank', models.CharField(blank=True, choices=[('1', 'BANCO DE CREDITO DEL PERU'), ('2', 'BANCO DE LA NACIÓN DEL PERU'), ('3', 'INTERBANK'), ('4', 'BBVA CONTINENTAL')], max_length=1, null=True, verbose_name='Banco')),
                ('code_operation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Coidgo de operacion')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Monto de pago')),
                ('date_payment', models.DateTimeField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('casing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.Casing')),
                ('coin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.Coin')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.Order')),
                ('subsidiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrm.Subsidiary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Registro de pago',
                'verbose_name_plural': 'Registros de pagos',
            },
        ),
    ]