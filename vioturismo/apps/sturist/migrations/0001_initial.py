# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vioturismo.apps.sturist.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='experiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('contacto2', models.CharField(max_length=200)),
                ('telefono2', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='rutaSitio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('contacto2', models.CharField(max_length=200)),
                ('telefono2', models.CharField(max_length=200)),
                ('precio', models.DecimalField(max_digits=9, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='producto',
            name='rutas',
            field=models.ManyToManyField(to='sturist.rutaSitio', null=True, blank=True),
            preserve_default=True,
        ),
    ]
