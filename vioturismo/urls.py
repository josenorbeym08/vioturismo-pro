from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
import settings
from django.contrib import admin
from .views import *
from vioturismo.views import *


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('vioturismo.apps.sitios.urls')),
    url(r'^',include('vioturismo.apps.sturist.urls')),
    url(r'^',include('vioturismo.apps.webServices.wsSitiostcs.urls')),
#   
#    url(r'^',include('vioturismo.apps.webServices.wsProductos.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

    url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done/'},
        name="password_reset_confirm"),
    (r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



