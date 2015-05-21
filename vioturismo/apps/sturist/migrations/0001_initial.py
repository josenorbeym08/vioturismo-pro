# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vioturismo.apps.sturist.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
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
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
