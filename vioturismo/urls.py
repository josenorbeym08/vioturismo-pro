from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('vioturismo.apps.sitios.urls')),
    url(r'^',include('vioturismo.apps.sturist.urls')),
    url(r'^',include('vioturismo.apps.webServices.wsSitiostcs.urls')),
#   
#    url(r'^',include('vioturismo.apps.webServices.wsProductos.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

)
