from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('FormularioProductos/', views.FormularioProductos),
    path('pruebaformulario/', views.pruebaformulario),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<codigo_producto>/', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminacionProducto/<codigo_producto>/', views.eliminacionProducto)

]