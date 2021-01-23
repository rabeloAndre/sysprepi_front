from django.contrib import admin
from django.urls import path
from front import views as views_front

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_front.index, name='index'),
    path('consulta', views_front.consulta, name='consulta'),
    path('login', views_front.login, name='login'),
    path('criar-conta', views_front.criarConta, name='criarConta'),
    path('index-socio', views_front.indexSocio, name='indexSocio'),
    path('solicitar-consulta', views_front.solicitarConsulta, name='solicitarConsulta'),


]
