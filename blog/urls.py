from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.post_list, name='post_list'),
    path('proyectos', views.proyectos, name='proyectos'),
    ]