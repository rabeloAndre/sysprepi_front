from django.contrib import admin
from django.urls import path
from front import views as views_front

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_front.init, name='init'),
]
