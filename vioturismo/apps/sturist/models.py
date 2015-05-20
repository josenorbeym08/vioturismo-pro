from django.db import models



def url(self,filename):
	ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
	return ruta



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

	def __unicode__(self):
		return self.nombre
	#def __unicode__(self):
	#	nombrecompleto = "%s %s"%(self.nombre,self.descripcion)
	#	return nombrecompleto
