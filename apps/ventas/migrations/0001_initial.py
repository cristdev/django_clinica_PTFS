# Generated by Django 3.1.3 on 2020-11-30 02:25

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
            name='PedidosCab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('O', 'Pedido'), ('T', 'Taller'), ('F', 'Finalizado')], max_length=1)),
                ('fecha', models.DateField()),
                ('pago', models.CharField(choices=[('C', 'Credito'), ('D', 'Debito'), ('V', 'Billetera virtual'), ('E', 'Efectivo')], max_length=1)),
                ('vendedor', models.ForeignKey(limit_choices_to={'groups__name': 'Venta'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('clasificacion', models.CharField(choices=[('L', 'Lentes'), ('O', 'Otros')], max_length=1)),
                ('lado', models.CharField(choices=[('I', 'Izquierda'), ('D', 'Derecha')], max_length=1, null=True)),
                ('cercania', models.CharField(choices=[('L', 'Lejos'), ('C', 'Cerca')], max_length=1, null=True)),
                ('armazon', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PedidosDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('unitario', models.FloatField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.pedidoscab')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.productos')),
            ],
        ),
    ]