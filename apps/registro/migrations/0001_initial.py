# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0001_initial'),
        ('centro_votacion', '0001_initial'),
        ('municipios', '0001_initial'),
        ('parroquias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroElectoral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nac', models.CharField(default=b'V', max_length=1, verbose_name=b'Nacionalidad', choices=[(b'V', b'Venezolano'), (b'E', b'Extranjero')])),
                ('cedula', models.CharField(max_length=8, unique=True, null=True, verbose_name=b'C\xc3\xa9dula')),
                ('p_apellido', models.CharField(max_length=200, null=True, verbose_name=b'Primer Apellido')),
                ('s_apellido', models.CharField(max_length=200, null=True, verbose_name=b'Segundo Apellido')),
                ('p_nombre', models.CharField(max_length=200, null=True, verbose_name=b'Primer Nombre')),
                ('s_nombre', models.CharField(max_length=200, null=True, verbose_name=b'Segundo Nombre')),
                ('f_nac', models.DateField(null=True, verbose_name=b'Fecha de nacimiento')),
                ('sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('cod_viejo', models.CharField(max_length=20, null=True, verbose_name=b'C\xc3\xb3digo anterior')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.CharField(max_length=15, null=True)),
                ('mun', models.CharField(max_length=30, null=True)),
                ('cod_estado', models.ForeignKey(related_name='estado_registro', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_estado', to='estados.Estado', null=True)),
                ('cod_municipio', models.ForeignKey(to='municipios.Municipio')),
                ('cod_nuevo', models.ForeignKey(related_name='centro_registro', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_n', to='centro_votacion.CentroVotacion', null=True)),
                ('cod_parroquia', models.ForeignKey(to='parroquias.Parroquia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
