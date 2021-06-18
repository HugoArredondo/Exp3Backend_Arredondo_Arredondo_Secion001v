from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nosotros/', views.about, name="about"),
    path('trabajos/', views.job, name="job"),
    path('cotizar/', views.cotizar, name="cotizar"),
    path('inicio_sesion/', views.iniciosesion, name="iniciosesion"),
    path('registro/', views.registrarse, name="registro"),
]