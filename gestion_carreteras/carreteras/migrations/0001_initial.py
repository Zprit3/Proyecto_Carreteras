# Generated by Django 5.1.4 on 2024-12-08 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaCarretera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carretera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carreteras.categoriacarretera')),
            ],
        ),
        migrations.CreateModel(
            name='Tramo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km_inicio', models.FloatField()),
                ('km_termino', models.FloatField()),
                ('es_inicio_carretera', models.BooleanField(default=False)),
                ('es_fin_carretera', models.BooleanField(default=False)),
                ('km_confluencia', models.FloatField(blank=True, null=True)),
                ('carretera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carreteras.carretera')),
                ('comuna_confluencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confluencias', to='carreteras.comuna')),
                ('comuna_inicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tramos_inicio', to='carreteras.comuna')),
                ('comuna_termino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tramos_termino', to='carreteras.comuna')),
                ('confluye_con', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confluencias', to='carreteras.carretera')),
            ],
        ),
    ]
