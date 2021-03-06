"""emprestimo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = "index"),
    url(r'central/$', views.central), 
    url(r'criar/$', views.criar_usuario, name = "criar" ),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'reset/$', views.passwordReset, name='passwordReset'),
    url(r'^(?P<pk>\d+)/$', views.detalhes_objeto, name='detalhes'),
    url(r'^criarobj/$', views.criar_objetos, name='criarobj'),
]
