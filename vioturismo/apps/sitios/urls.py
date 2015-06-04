from django.conf.urls import patterns,url


urlpatterns = patterns('vioturismo.apps.sitios.views',
    url(r'^$','index_view', name="vista_principal"),
    url(r'^about/$','about_view',name='vista_about'),
    
    url(r'^login/$','login_view', name='vista_login'),
    url(r'^registro/$','register_view', name='vista_registro'),
    url(r'^logout/$','logout_view', name='vista_logout'),
    url(r'^sitiosts/page/(?P<pagina>.*)/$','productos_view',name='vista_productos'),

    url(r'^servicios/page/(?P<pagina>.*)/$','servicios_view',name='vista_servicios'),
    
	url(r'^experiencias/page/(?P<pagina>.*)/$','experiencias_view',name='vista_experiencias'),

    url(r'^sitiost/(?P<id_prod>.*)/$','singleProduct_view',name='vista_single_producto'),

    url(r'^experiencia/(?P<id_expe>.*)/$','singleExperinc_view',name='vista_single_experiencia'),


    url(r'^servicio/(?P<id_serv>.*)/$','singleServic_view',name='vista_single_servicio'),
    
    url(r'^contacto/$','contacto_view',name='vista_contacto'),
        


)
