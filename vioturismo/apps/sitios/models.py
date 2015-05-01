#coding: utf-8
from django.db import models


class sitio(models.Model):
	nombre			= models.CharField(max_length=200)
	descripcion		= models.CharField(max_length=200)
	contacto		= models.CharField(max_length=200)
	status			= models.BooleanField(default=True)

	def __unicode__(self):
		nombrecompleto = "%s %s"%(self.nombre,self.descripcion)
		return nombrecompleto
