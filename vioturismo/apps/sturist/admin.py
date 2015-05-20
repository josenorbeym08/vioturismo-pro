from django.contrib import admin
from vioturismo.apps.sturist.models import producto


class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'thumbnail','contacto')
	list_filter = ('nombre', 'contacto')
	search_fields = ['nombre','contacto']
	fields =('nombre','descripcion','contacto','imagen','status')






admin.site.register(producto,productoAdmin)
