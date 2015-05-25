from django.contrib import admin
from vioturismo.apps.sturist.models import producto
from vioturismo.apps.sturist.models import servicio


class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail','contacto')
	list_filter = ('nombre', 'contacto')
	search_fields = ['nombre','contacto']
	fields =('nombre','descripcion','contacto','imagen','status')




class servicioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail','contacto','precio')
	list_filter = ('nombre', 'contacto','precio')
	search_fields = ['nombre','contacto']
	fields =('nombre','descripcion','contacto','imagen','precio','status')



admin.site.register(producto,productoAdmin)
admin.site.register(servicio,servicioAdmin)
