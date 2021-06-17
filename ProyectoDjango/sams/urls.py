from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="inicio"),
    path('nosotros/', views.about, name="nosotros"),
    path('trabajos/', views.job, name="trabajos"),
    path('cotizar/', views.cotizar, name="cotizar"),
    path('inicio_sesion/', views.iniciosesion, name="iniciosesion"),
    path('registro/', views.registrarse, name="registro"),
]