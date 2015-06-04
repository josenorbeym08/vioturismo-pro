from django.db import models



def url(self,filename):
	ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
	return ruta



def url(self,filename):
	ruta = "MultimediaData/Servicio/%s/%s"%(self.nombre,str(filename))
	return ruta




def url(self,filename):
	ruta = "MultimediaData/Experiencia/%s/%s"%(self.nombre,str(filename))
	return ruta






class rutaSitio(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion= models.TextField(max_length=400)

	def __unicode__(self):
		return self.nombre




class producto(models.Model):

#	def url(self,filename):
#		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
#		return ruta

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True

	nombre			= models.CharField(max_length=100)
	descripcion		= models.TextField(max_length=300)
	status			= models.BooleanField(default=True)
	imagen          = models.ImageField(upload_to=url,null=True,blank=True)
	contacto		= models.CharField(max_length=200)
	telefono        = models.CharField(max_length=200)
	contacto2       = models.CharField(max_length=200)
	telefono2       = models.CharField(max_length=200)
	rutas           = models.ManyToManyField(rutaSitio,null=True,blank=True)


	def __unicode__(self):
		return self.nombre
	#def __unicode__(self):
	#	nombrecompleto = "%s %s"%(self.nombre,self.descripcion)
	#	return nombrecompleto


class servicio(models.Model):

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True
	nombre			= models.CharField(max_length=100)
	descripcion		= models.TextField(max_length=300)
	status			= models.BooleanField(default=True)
	imagen          = models.ImageField(upload_to=url,null=True,blank=True)
	contacto		= models.CharField(max_length=200)
	telefono		= models.CharField(max_length=200)
	contacto2       = models.CharField(max_length=200)
	telefono2       = models.CharField(max_length=200)
	precio			= models.DecimalField(max_digits=9,decimal_places=2)


	def __unicode__(self):
		return self.nombre
	

class experiencia(models.Model):

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	imagen          = models.ImageField(upload_to=url,null=True,blank=True)
	thumbnail.allow_tags = True
	nombre			= models.CharField(max_length=100)
	descripcion		= models.CharField(max_length=300)
	status			= models.BooleanField(default=True)
	
	

	def __unicode__(self):
		return self.nombre




