from django.shortcuts import render_to_response
from django.template import RequestContext
from vioturismo.apps.sturist.forms import addProductForm
from vioturismo.apps.sturist.models import producto 
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method =="POST":
			form = addProductForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen']
				contacto = form.cleaned_data['contacto']
				p = producto()
				if imagen:
					p.imagen = imagen
				p.nombre = nombre
				p.descripcion = descripcion
				p.contacto    = contacto
				p.status = True
				p.save()
				info = "se guardo satisfactoriamente !!!!"
			else:
				info = "informacion con datos incorrectos"
		form = addProductForm()
		ctx = {'form':form, 'informacion':info}
		return render_to_response('sturist/addProducto.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
