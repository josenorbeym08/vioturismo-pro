from django.conf.urls import patterns, url

urlpatterns = patterns(
	'vioturismo.apps.sturist.views',
	url(r'^add/sitiost/$','add_product_view', name= "vista_agregar_producto"),
	url(r'^add/servicio/$','add_servic_view', name= "vista_agregar_servicio"),
	url(r'^add/experiencia/$','add_experienc_view', name= "vista_agregar_experiencia"),
	url(r'^edit/sitiost/(?P<id_prod>.*)/$','edit_product_view', name= "vista_editar_producto"),
	url(r'^edit/servicio/(?P<id_serv>.*)/$','edit_servic_view', name= "vista_editar_servicio"),
	url(r'^edit/experiencia/(?P<id_expe>.*)/$','edit_experienc_view', name= "vista_editar_experiencia"),
)