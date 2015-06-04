from django.shortcuts import render_to_response
from django.template import RequestContext
from vioturismo.apps.sturist.forms import addProductForm
from vioturismo.apps.sturist.forms import addServicForm
from vioturismo.apps.sturist.forms import addExperiencForm

from vioturismo.apps.sturist.models import producto
from vioturismo.apps.sturist.models import servicio
from vioturismo.apps.sturist.models import experiencia
from django.http import HttpResponseRedirect



def edit_product_view(request,id_prod):
	info = "iniciado"
	prod = producto.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			form.save_m2m()
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/sitiost/%s/'%edit_prod.id)
	else:
		form = addProductForm(instance=prod)
	ctx = {'form':form,'informacion':info}
	return render_to_response('sturist/editProducto.html',ctx,context_instance=RequestContext(request))


def add_product_view(request):
	info = "iniciado"
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save() # Guardamos la informacion
			form.save_m2m() # Guarda las relaciones de ManyToMany
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/sitiost/%s'%add.id)
	else:
		form = addProductForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('sturist/addProducto.html',ctx,context_instance=RequestContext(request)) 






"""
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

"""


def edit_servic_view(request,id_serv):
	info = "iniciado"
	serv = servicio.objects.get(pk=id_serv)
	if request.method == "POST":
		form = addServicForm(request.POST,request.FILES,instance=serv)
		if form.is_valid():
			edit_serv = form.save(commit=False)
			form.save_m2m()
			edit_serv.status = True
			edit_serv.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/servicio/%s/'%edit_serv.id)
	else:
		form = addServicForm(instance=serv)
	ctx = {'form':form,'informacion':info}
	return render_to_response('sturist/editServicio.html',ctx,context_instance=RequestContext(request))





def add_servic_view(request):
	info = "iniciado"
	if request.method == "POST":
		form = addServicForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save() # Guardamos la informacion
			form.save_m2m() # Guarda las relaciones de ManyToMany
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/servicio/%s'%add.id)
	else:
		form = addServicForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('sturist/addServicio.html',ctx,context_instance=RequestContext(request)) 





"""
def add_servic_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method =="POST":
			form = addServicForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen']
				contacto = form.cleaned_data['contacto']
				precio = form.cleaned_data['precio']
				s = servicio()
				if imagen:
					s.imagen = imagen
				s.nombre = nombre
				s.descripcion = descripcion
				s.contacto    = contacto
				s.precio = precio
				s.status = True
				s.save()
				info = "se guardo satisfactoriamente !!!!"
			else:
				info = "informacion con datos incorrectos"
		form = addServicForm()
		ctx = {'form':form, 'informacion':info}
		return render_to_response('sturist/addServicio.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

"""


def edit_experienc_view(request,id_expe):
	info = "iniciado"
	expe = experiencia.objects.get(pk=id_expe)
	if request.method == "POST":
		form = addExperiencForm(request.POST,request.FILES,instance=expe)
		if form.is_valid():
			edit_expe = form.save(commit=False)
			form.save_m2m()
			edit_expe.status = True
			edit_expe.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('/experiencia/%s/'%edit_expe.id)
	else:
		form = addExperiencForm(instance=expe)
	ctx = {'form':form,'informacion':info}
	return render_to_response('sturist/editExperiencia.html',ctx,context_instance=RequestContext(request))





def add_experienc_view(request):
	info = "iniciado"
	if request.method == "POST":
		form = addExperiencForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save() # Guardamos la informacion
			form.save_m2m() # Guarda las relaciones de ManyToMany
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/experiencia/%s'%add.id)
	else:
		form = addExperiencForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('sturist/addExperiencia.html',ctx,context_instance=RequestContext(request)) 




"""

def add_experienc_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method =="POST":
			form = addExperiencForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen']
				e = experiencia()
				if imagen:
					e.imagen = imagen
				e.nombre = nombre
				e.descripcion = descripcion
				e.status = True
				e.save()
				info = "se guardo satisfactoriamente !!!!"
			else:
				info = "informacion con datos incorrectos"
		form = addExperiencForm()
		ctx = {'form':form, 'informacion':info}
		return render_to_response('sturist/addExperiencia.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

"""
