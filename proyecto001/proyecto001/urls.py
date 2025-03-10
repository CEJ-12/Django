"""
URL configuration for proyecto001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name = "saludo"),
    path('', views.index, name="index"),
    path('rango/', views.rango, name="rango"),   
    path('buscar-articulo/<int:id>/', views.buscar_articulo, name="buscar_articulo"),
    path('editar-articulo/<int:id>',views.editar_articulo,name="editar_articulo"),
    path('listar-articulos/', views.listar_articulos, name="listar_articulos"),
    path('eliminar-articulo/<int:id>',views.eliminar_articulo, name='eliminar_articulo'),
    path('save-articulo/',views.save_articulo, name='save_articulo'),
    path('create-articulo/',views.create_articulo, name='create_articulo'),
    path('create-autor/',views.create_autor, name="create_autor" ),
    path('save-autor/',views.save_autor, name="save_autor"),
    path('create-full-articulo/',views.create_full_articulo, name='create_full_articulo'),
]
