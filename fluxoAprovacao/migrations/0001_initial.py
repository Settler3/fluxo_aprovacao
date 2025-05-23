# Generated by Django 5.2 on 2025-04-05 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('esteira', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FluxoAprovacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Fluxo de Aprovação',
                'verbose_name_plural': 'Fluxos de Aprovação',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='EtapaFluxo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ordem', models.IntegerField()),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fluxos_aprovacao', to='esteira.etapa')),
                ('fluxo_aprovacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etapas', to='fluxoAprovacao.fluxoaprovacao')),
            ],
            options={
                'verbose_name': 'Etapa do Fluxo de Aprovação',
                'verbose_name_plural': 'Etapas do Fluxo de Aprovação',
                'ordering': ['ordem'],
                'indexes': [models.Index(fields=['fluxo_aprovacao', 'etapa'], name='fluxoAprova_fluxo_a_8998dd_idx')],
                'constraints': [models.UniqueConstraint(fields=('fluxo_aprovacao', 'etapa'), name='unique_fluxo_etapa')],
            },
        ),
    ]
