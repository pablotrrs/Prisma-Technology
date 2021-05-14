from django.urls import path
from .views import ListarSucursal, RegistrarSucursal,EliminarSucursal, idSucursal, idCaja
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('listado_sucursales/', login_required(ListarSucursal.as_view()) ,name='listar_sucursales'),
    path('registrar_sucursal/', login_required(RegistrarSucursal.as_view()),name = 'registrar_sucursal'),
    path('eliminar_sucursal/<int:pk>/',login_required(EliminarSucursal.as_view()), name='eliminar_sucursal'),
    path('visualizar_items/<int:id>/', login_required(idSucursal), name= 'visualizar_items'),
    path('visualizar_cajas/<int:id>/', login_required(idCaja), name= 'visualizar_cajas'),
    
]