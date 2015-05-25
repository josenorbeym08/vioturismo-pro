from django.shortcuts import render_to_response
from django.template import RequestContext
from vioturismo.apps.sitios.forms import loginForm, RegisterForm, ContactForm
from vioturismo.apps.sturist.models import producto
from vioturismo.apps.sturist.models import servicio
from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect 
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index_view(request):
    return render_to_response('sitios/index.html',context_instance=RequestContext(request))

def productos_view(request,pagina):
    lista_prod = producto.objects.filter(status=True)
    paginator = Paginator(lista_prod,5)
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        productos = paginator.page(page)
    except (EmptyPage,InvalidPage):
        productos = paginator.page(paginator.num_pages)
    ctx = {'productos':productos}
    return render_to_response('sitios/productos.html',ctx,context_instance=RequestContext(request))


def singleProduct_view(request,id_prod):
    prod = producto.objects.get(id=id_prod)
    ctx = {'producto':prod}
    return render_to_response('sitios/SingleProducto.html',ctx,context_instance=RequestContext(request))



def servicios_view(request,pagina):
    lista_serv = servicio.objects.filter(status=True)
    paginator = Paginator(lista_serv,5)
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        servicios = paginator.page(page)
    except (EmptyPage,InvalidPage):
        servicios = paginator.page(paginator.num_pages)
    ctx = {'servicios':servicios}
    return render_to_response('sitios/servicios.html',ctx,context_instance=RequestContext(request))



def singleServic_view(request,id_serv):
    serv = servicio.objects.get(id=id_serv)
    ctx = {'servicio':serv}
    return render_to_response('sitios/SingleServicio.html',ctx,context_instance=RequestContext(request))




def contacto_view(request):
    info_enviado = False
    email = ""
    titulo = ""
    texto = ""
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
           info_enviado = True
           email = formulario.cleaned_data['Email']
           titulo =formulario.cleaned_data['Titulo']
           texto = formulario.cleaned_data['Texto']

           to_admin = 'sanchezmoralesjn@gmail.com'
           html_content = "Informacion recibida de [%s] <br><br><br>***Mensaje***<br><br>%s"%(email,texto)
           msg = EmailMultiAlternatives('Correo de Contacto', html_content,'from@server.com',[to_admin])
           msg.attach_alternative(html_content,'text/html')
           msg.send()
    else:                
        formulario = ContactForm()
    ctx = {'form':formulario, 'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
    return render_to_response('sitios/contacto.html',ctx,context_instance=RequestContext(request))



def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = loginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "usuario y/o password incorrectos"
        form = loginForm()
        ctx = {'form': form,'mensaje':mensaje}
        return render_to_response('sitios/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    form = RegisterForm()
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(username=usuario,email=email,password=password_one)
            u.save()
            return render_to_response('sitios/thanks_register.html',context_instance=RequestContext(request))
        else:
            ctx = {'form':form}
            return render_to_response('sitios/register.html',ctx,context_instance=RequestContext(request))  
    ctx = {'form': form}
    return render_to_response('sitios/register.html',ctx,context_instance=RequestContext(request))
