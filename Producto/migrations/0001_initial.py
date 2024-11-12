# Generated by Django 5.0.9 on 2024-11-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('nombre_producto', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=20)),
                ('stock_min', models.IntegerField()),
                ('stock_max', models.IntegerField()),
                ('codigo_producto', models.CharField(max_length=50, unique=True)),
                ('unidad', models.CharField(max_length=20)),
                ('cant_stock', models.IntegerField()),
                ('Estado', models.CharField(max_length=20)),
                ('observaciones', models.CharField(max_length=75)),
            ],
        ),
    ]