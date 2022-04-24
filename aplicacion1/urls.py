from django.urls import path, include
from  .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('formulario_usuario/', views.formulario_usuario, name='formulario_usuario'),
]
