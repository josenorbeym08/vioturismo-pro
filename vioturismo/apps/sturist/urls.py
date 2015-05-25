from django.conf.urls import patterns, url

urlpatterns = patterns(
	'vioturismo.apps.sturist.views',
	url(r'^add/sitiost/$','add_product_view', name= "vista_agregar_producto"),
	url(r'^add/servicio/$','add_servic_view', name= "vista_agregar_servicio"),

)