from django.conf.urls import patterns, url




urlpatterns = patterns(	'vioturismo.apps.webServices.wsSitiostcs.views',
	url(r'^ws/sitiosts/$','wsSitiostcs_view', name= "ws_sitiosts_url"),
	
)