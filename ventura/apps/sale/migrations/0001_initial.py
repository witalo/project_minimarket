# Generated by Django 3.0.5 on 2021-02-07 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0001_initial'),
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_document', models.CharField(choices=[('01', 'DNI'), ('06', 'RUC'), ('07', 'PASAPORTE'), ('04', 'CARNET DE EXTRANJERÍA')], default='01', max_length=2, verbose_name='Tipo Documento')),
                ('document', models.CharField(blank=True, max_length=15, null=True)),
                ('full_names', models.CharField(blank=True, max_length=200, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=9, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_coin', models.CharField(max_length=50, unique=True, verbose_name='Nombre moneda')),
                ('abbreviation', models.CharField(blank=True, max_length=5, null=True, verbose_name='Abreviatura')),
                ('is_enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Moneda',
                'verbose_name_plural': 'Monedas',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('T', 'Cotización'), ('V', 'Venta'), ('R', 'Requerimiento'), ('C', 'Compra'), ('F', 'Fabricacion')], default='T', max_length=1, verbose_name='Tipo')),
                ('invoice', models.CharField(blank=True, max_length=100, null=True, verbose_name='Comprobante')),
                ('correlative_order', models.IntegerField(default=0, verbose_name='Correlativo de la orden')),
                ('status', models.CharField(choices=[('P', 'Pendiente'), ('C', 'Completado'), ('A', 'Anulado')], default='P', max_length=1, verbose_name='Estado')),
                ('create_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Descuento')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.Client', verbose_name='Cliente')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase.Provider', verbose_name='Proveedor')),
                ('subsidiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrm.Subsidiary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Codigo')),
                ('names', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('stock_min', models.DecimalField(decimal_places=4, default=0, max_digits=30, verbose_name='Stock Minimo')),
                ('stock_max', models.DecimalField(decimal_places=4, default=0, max_digits=30, verbose_name='Stock Maximo')),
                ('type', models.CharField(choices=[('1', 'Bienes de uso común'), ('2', 'Bienes de consumo'), ('3', 'Bienes de emergencia'), ('4', 'Bienes durables'), ('5', 'Bienes de especialidad'), ('6', 'Servicios')], default='1', max_length=1, verbose_name='Tipo')),
                ('photo', models.ImageField(blank=True, default='product/product0.jpg', upload_to='product/')),
                ('is_state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=5, unique=True, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripción')),
                ('is_enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Unidad de medida',
                'verbose_name_plural': 'Unidades de medida',
            },
        ),
        migrations.CreateModel(
            name='SubsidiaryStore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('category', models.CharField(choices=[('1', 'Materias primas'), ('2', 'Productos intermedios'), ('3', 'Productos terminados'), ('4', 'Equipos'), ('5', 'Accesorios')], default='1', max_length=1, verbose_name='Categoria')),
                ('subsidiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrm.Subsidiary')),
            ],
            options={
                'verbose_name': 'Almacén de sede',
                'verbose_name_plural': 'Almacenes de sede',
                'unique_together': {('subsidiary', 'category')},
            },
        ),
        migrations.CreateModel(
            name='RecipeDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio Unitario')),
                ('product_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='sale.Product')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Unit')),
            ],
            options={
                'verbose_name': 'Detalle de Receta',
                'verbose_name_plural': 'Detalles de Recetas',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='sale.Product')),
                ('subsidiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrm.Subsidiary')),
            ],
            options={
                'verbose_name': 'Registro de Receta',
                'verbose_name_plural': 'Registros de Recetas',
            },
        ),
        migrations.CreateModel(
            name='ProductStore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.DecimalField(decimal_places=4, default=0, max_digits=30, verbose_name='Stock')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Product', verbose_name='Producto')),
                ('subsidiary_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='sale.SubsidiaryStore', verbose_name='Almacen sede')),
            ],
            options={
                'verbose_name': 'Almacén de producto',
                'verbose_name_plural': 'Almacenes de producto',
                'unique_together': {('product', 'subsidiary_store')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.ProductCategory'),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad')),
                ('price_unit', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio unitario')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Product')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Unit')),
            ],
            options={
                'verbose_name': 'Detalle venta',
                'verbose_name_plural': 'Detalles venta',
            },
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operation', models.CharField(choices=[('C', 'Inicial'), ('E', 'Entrada'), ('S', 'Salida'), ('R', 'Reajuste')], default='C', max_length=1, verbose_name='Operación')),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad')),
                ('price_unit', models.DecimalField(decimal_places=15, default=0, max_digits=30, verbose_name='Precio unitario')),
                ('price_total', models.DecimalField(decimal_places=15, default=0, max_digits=30, verbose_name='Precio total')),
                ('remaining_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad restante')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('order_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.OrderDetail')),
                ('product_store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.ProductStore')),
            ],
            options={
                'verbose_name': 'Registro de Kardex',
                'verbose_name_plural': 'Registros de Kardex',
            },
        ),
        migrations.CreateModel(
            name='ProductPresenting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price_sale', models.DecimalField(decimal_places=4, default=0, max_digits=30, verbose_name='Precio de Venta')),
                ('quantity_minimum', models.DecimalField(decimal_places=4, default=0, max_digits=30, verbose_name='Cantidad Minima')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Coin')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Product')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Unit')),
            ],
            options={
                'verbose_name': 'Presentación',
                'verbose_name_plural': 'Presentaciones',
                'unique_together': {('product', 'unit', 'coin')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('names', 'code')},
        ),
        migrations.CreateModel(
            name='OrderBill',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sale.Order')),
                ('type', models.CharField(choices=[('1', 'Factura'), ('2', 'Boleta')], max_length=2, verbose_name='Tipo de Comprobante')),
                ('serial', models.CharField(blank=True, max_length=5, null=True, verbose_name='Serie')),
                ('number_receipt', models.IntegerField(default=0, verbose_name='Numero de Comprobante')),
                ('sunat_status', models.CharField(blank=True, max_length=5, null=True, verbose_name='Sunat Status')),
                ('sunat_description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sunat descripcion')),
                ('sunat_enlace_pdf', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sunat Enlace Pdf')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('code_qr', models.CharField(blank=True, max_length=500, null=True, verbose_name='Codigo QR')),
                ('code_hash', models.CharField(blank=True, max_length=500, null=True, verbose_name='Codigo Hash')),
                ('status', models.CharField(choices=[('E', 'Emitido'), ('A', 'Anulado')], max_length=1, verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Registro de comprobante',
                'verbose_name_plural': 'Registros de comprobantes',
            },
        ),
    ]
