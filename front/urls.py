from django.contrib import admin
from django.urls import path
from front import views as views_front

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_front.index, name='index'),
    path('consulta/', views_front.consulta, name='consulta'),

]
