from django.contrib import admin
from vioturismo.apps.sturist.models import producto
from vioturismo.apps.sturist.models import servicio
from vioturismo.apps.sturist.models import experiencia
from vioturismo.apps.sturist.models import rutaSitio

class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail','contacto','telefono','contacto2','telefono2')
	list_filter = ('nombre', 'contacto','telefono','contacto2','telefono2')
	search_fields = ['nombre','contacto','telefono','contacto2','telefono2']
	fields =('nombre','descripcion','contacto','telefono','imagen','rutas','status','contacto2','telefono2')




class servicioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail','contacto','precio','telefono','contacto2','telefono2')
	list_filter = ('nombre', 'contacto','precio','telefono','contacto2','telefono2')
	search_fields = ['nombre','contacto','telefono','contacto2','telefono2']
	fields =('nombre','descripcion','contacto','telefono','imagen','precio','status','contacto2','telefono2')



class experienciaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail','descripcion')
	list_filter = ('nombre', 'descripcion')
	search_fields = ['nombre','descripcion']
	fields =('nombre','descripcion','imagen','status')






admin.site.register(producto,productoAdmin)
admin.site.register(servicio,servicioAdmin)
admin.site.register(experiencia,experienciaAdmin)
admin.site.register(rutaSitio)