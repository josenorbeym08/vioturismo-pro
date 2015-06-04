from django.db import models
from django.contrib.auth.models import User
#from django.conf.urls.static import static


#def image_path(filename):
#	ruta = "settings/%s/%s" % (self.settings_name, str(filename))
#	return ruta


def url(self,filename):
	ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
	return ruta


class userProfile(models.Model):

#	def url(self,filename):
#		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
#		return ruta

	user     = models.OneToOneField(User)
	photo    = models.ImageField(upload_to=url)
	telefono = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.user.username



#class Setting(models.Model):
#	def image_path(self,filename):
#		ruta = "settings/%s/%s" % (self.settings_name, str(filename))
#		return ruta


#	settings_name = models.CharField(max_length=200)
#	my_name = models.CharField(max_length=200)
#	my_job = models.CharField(max_length=200)
#	my_description = models.TextField(max_length=500)
#	my_photo = models.ImageField(upload_to= image_path)
#	background = models.ImageField(upload_to= image_path)
#	status = models.BooleanField(default=False)
#	def __unicode__(self):
#		return self.settings_name

#	class Meta:
#		verbose_name = "Configuracion de la web"
#		verbose_name_plural = "configuraciones de la web"









