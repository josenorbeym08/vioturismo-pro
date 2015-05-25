#from django.shortcuts import render

from django.http import HttpResponse
from vioturismo.apps.sturist.models import producto

from django.core import serializers


def wsSitiostcs_view(request):
	data = serializers.serialize("xml",producto.objects.filter(status=True))
	return HttpResponse(data,'application/xml')
