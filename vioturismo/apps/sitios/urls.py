from django.conf.urls import patterns,url


urlpatterns = patterns('vioturismo.apps.sitios.views',
    url(r'^$','index_view', name="vista_principal"),
    url(r'^login/$','login_view', name='vista_login'),
    url(r'^registro/$','register_view', name='vista_registro'),
    url(r'^logout/$','logout_view', name='vista_logout'),
    url(r'^productos/page/(?P<pagina>.*)/$','productos_view',name='vista_productos'),

    url(r'^servicios/page/(?P<pagina>.*)/$','servicios_view',name='vista_servicios'),
    
    url(r'^producto/(?P<id_prod>.*)/$','singleProduct_view',name='vista_single_producto'),
    
    url(r'^servicio/(?P<id_prod>.*)/$','singleProduct_view',name='vista_single_producto'),
    
    url(r'^contacto/$','contacto_view',name='vista_contacto'),
        


)
