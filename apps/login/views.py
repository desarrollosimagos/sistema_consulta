# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, FormView
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib import messages # Metodo para la validacion de los campos
from apps.login.forms import LoginForm, UserForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from .models import PerfilesUsuario

class RegistrarseUsuario(FormView):
    template_name = 'usuario/registro/registro_user.html'
    form_class    = UserForm
    success_url   = reverse_lazy('Login')

    def form_valid(self, form):
        user        = form.save()
        perfil      = PerfilesUsuario()
        perfil.user = user
        perfil.tlf  = form.cleaned_data['tlf']
        perfil.user_accion = form.cleaned_data['user_accion']
        perfil.save()
        return super(RegistrarseUsuario, self).form_valid(form)

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario  = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/')
                else:
                    if usuario is not None:
                        mensaje = "Usuario inactivo"
                    else:
                        mensaje = "Usuario y/o Contraseña incorrecto"
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje}
        return render_to_response('usuario/login/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')