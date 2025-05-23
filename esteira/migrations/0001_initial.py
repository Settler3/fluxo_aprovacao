# Generated by Django 5.2 on 2025-04-05 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esteira',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Esteira',
                'verbose_name_plural': 'Esteiras',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Etapa',
                'verbose_name_plural': 'Etapas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='EsteiraFluxo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ordem', models.IntegerField()),
                ('esteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fluxos', to='esteira.esteira')),
            ],
            options={
                'verbose_name': 'Esteira do Fluxo de Aprovação',
                'verbose_name_plural': 'Esteiras do Fluxo de Aprovação',
                'ordering': ['ordem'],
            },
        ),
    ]
