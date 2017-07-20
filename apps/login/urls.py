from django.conf.urls import url
from .views import login_view, logout_view, RegistrarseUsuario

urlpatterns = [
	url(r'^nuevo_usuario/$',RegistrarseUsuario.as_view(), name="nuevo_usuario",),
    url(r'^login/$', 'apps.login.views.login_view', name="Login",),
    url(r'^logout/$', 'apps.login.views.logout_view', name="Logout",),
]
