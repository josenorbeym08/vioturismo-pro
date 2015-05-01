__author__ = 'ASUS I5'

from django.conf.urls import patterns, url


urlpatterns = patterns('vioturismo.apps.sitios.views',
                       url(r'^$','index_view', name="url_index"),

                       url(r'^login/$','login_view', name='vista_login'),
                       url(r'^registro/$','register_view', name='vista_registro'),
                       url(r'^logout/$','logout_view', name='vista_logout'),


                       )
