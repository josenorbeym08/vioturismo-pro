from django.contrib import admin
from vioturismo.apps.sitios.models import Setting 
 

from vioturismo.apps.sitios.models import userProfile

admin.site.register(userProfile)
admin.site.register(Setting)


