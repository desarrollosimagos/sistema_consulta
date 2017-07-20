# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroVotacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('municipio', models.IntegerField(null=True)),
                ('parroquia', models.IntegerField(null=True)),
                ('id_mun', models.IntegerField(null=True)),
                ('cod_n', models.IntegerField(max_length=11, unique=True, null=True, verbose_name=b'Cod Nuevo')),
                ('cod_v', models.CharField(max_length=11, null=True, verbose_name=b'Cod Viejo')),
                ('c_votacion', models.TextField(max_length=1500, verbose_name=b'Centro de Votacion')),
                ('direccion', models.TextField(max_length=1500, verbose_name=b'Direccion')),
                ('user', models.CharField(max_length=15, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.ForeignKey(related_name='estado_centro_votacion', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
