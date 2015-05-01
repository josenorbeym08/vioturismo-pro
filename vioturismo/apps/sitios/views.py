from django.shortcuts import render, render_to_response, RequestContext

from vioturismo.apps.sitios.forms import loginForm, RegisterForm

from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponsePermanentRedirect


# Create your views here.

def index_view(request):
    return render_to_response('sitios/index.html', context_instance=RequestContext(request))



def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
            return HttpResponsePermanentRedirect('/')
    else:
            if request.method == "POST":
                form = loginForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    usuario = authenticate(username=username,password=password)
                    if usuario is not None and usuario.is_active:
                        login(request,usuario)
                        return HttpResponsePermanentRedirect('/')
                    else:
                            mensaje = "usuario y/o password incorrectos"
            form = loginForm()
            ctx = {'form': form, 'mensaje': mensaje}
            return render_to_response('sitios/login.html', ctx,context_instance=RequestContext(request))
def logout_view(request):
        logout(request)
        return HttpResponsePermanentRedirect('/')



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
