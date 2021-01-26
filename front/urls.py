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
    path('vizualizar-consultas-agendadas', views_front.vizualizarConsultasAgendadas, name='vizualizarConsultasAgendadas'),
    path('realizar-doacao', views_front.realizarDoacao, name='realizarDoacao'),
    path('vizualizar-doacoes-realizadas', views_front.vizualizarDoacoesRealizadas, name='vizualizarDoacoesRealizadas'),
    path('perfil-socio', views_front.perfilSocio, name='perfilSocio'),

]
